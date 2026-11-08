from __future__ import annotations

from dataclasses import replace

import pytest

from end_to_end_skill_validator import (
    CORE_SRS_COVERAGE,
    REQUIRED_CODING_GATES,
    SRS_COVERAGE,
    CoverageItem,
    GateResult,
    GateStatus,
    ReleaseEvidence,
    RepositoryValidation,
    SuiteResult,
    assess_srs_gate,
    coding_allowed,
    deployment_eligibility,
    discover_skills,
    production_verification,
)


def complete_srs_coverage() -> dict[str, CoverageItem]:
    return {area: CoverageItem("covered", "SRS:" + area) for area in SRS_COVERAGE}


def passed(candidate: str = "candidate-1") -> SuiteResult:
    return SuiteResult(True, "passed", candidate, "run://" + candidate)


def not_applicable(reason: str = "ordinary backend; no model") -> SuiteResult:
    return SuiteResult(False, "not_applicable", "", reason)


def complete_release_evidence(candidate: str = "candidate-1") -> ReleaseEvidence:
    return ReleaseEvidence(
        candidate=candidate,
        source_revision="commit-abc",
        artifact_digest="sha256:123",
        local_relevant_checks=passed(candidate),
        ci_unit=passed(candidate),
        ci_integration=passed(candidate),
        ci_contract=passed(candidate),
        ci_regression=passed(candidate),
        model_quality=not_applicable(),
        security=passed(candidate),
        prepromotion_smoke=passed(candidate),
        postdeployment_smoke=passed(candidate),
        rollback_ready=True,
        monitoring_ready=True,
    )


@pytest.mark.parametrize("missing_area", SRS_COVERAGE)
def test_every_missing_srs_coverage_area_blocks_g1(missing_area: str) -> None:
    coverage = complete_srs_coverage()
    del coverage[missing_area]

    result = assess_srs_gate(coverage)

    assert result.status is GateStatus.BLOCKED
    assert "coverage:" + missing_area in result.blockers


@pytest.mark.parametrize("core_area", sorted(CORE_SRS_COVERAGE))
def test_core_srs_coverage_cannot_be_not_applicable(core_area: str) -> None:
    coverage = complete_srs_coverage()
    coverage[core_area] = CoverageItem("not_applicable", "claimed irrelevant")

    result = assess_srs_gate(coverage)

    assert result.status is GateStatus.BLOCKED
    assert "coverage:" + core_area in result.blockers


def test_noncore_not_applicable_requires_a_reason() -> None:
    coverage = complete_srs_coverage()
    coverage["cancellation_expiry"] = CoverageItem("not_applicable", "")
    assert assess_srs_gate(coverage).status is GateStatus.BLOCKED

    coverage["cancellation_expiry"] = CoverageItem(
        "not_applicable", "request is synchronous and has no cancellable state"
    )
    assert assess_srs_gate(coverage).status is GateStatus.PASS


def test_open_critical_question_blocks_g1() -> None:
    result = assess_srs_gate(
        complete_srs_coverage(),
        critical_open_questions=("Q-authorization-owner",),
    )

    assert result.status is GateStatus.BLOCKED
    assert result.blockers == ("question:Q-authorization-owner",)


def test_conditional_g1_allows_only_named_independent_slice() -> None:
    coverage = complete_srs_coverage()
    del coverage["partial_failure_recovery"]
    result = assess_srs_gate(coverage, ready_slices=("read-only-search",))

    assert result.status is GateStatus.CONDITIONAL
    assert result.permits("read-only-search")
    assert not result.permits("write-ticket")


def test_complete_accepted_srs_coverage_passes_g1() -> None:
    result = assess_srs_gate(complete_srs_coverage())

    assert result.status is GateStatus.PASS
    assert not result.blockers
    assert len(result.evidence) == len(SRS_COVERAGE)


@pytest.mark.parametrize("missing_gate", REQUIRED_CODING_GATES)
def test_missing_required_gate_blocks_domain_coding(missing_gate: str) -> None:
    gates = {
        gate: GateResult(gate, GateStatus.PASS)
        for gate in REQUIRED_CODING_GATES
        if gate != missing_gate
    }

    allowed, blockers = coding_allowed(gates, "ticket-create")

    assert not allowed
    assert missing_gate + ":missing" in blockers


@pytest.mark.parametrize(
    "status", [GateStatus.BLOCKED, GateStatus.NOT_APPLICABLE]
)
def test_required_blocked_or_not_applicable_gate_blocks_coding(
    status: GateStatus,
) -> None:
    gates = {
        gate: GateResult(gate, GateStatus.PASS) for gate in REQUIRED_CODING_GATES
    }
    gates["G2_ARCHITECTURE_CONTRACTS"] = GateResult(
        "G2_ARCHITECTURE_CONTRACTS", status
    )

    allowed, blockers = coding_allowed(gates, "ticket-create")

    assert not allowed
    assert "G2_ARCHITECTURE_CONTRACTS:" + status.value in blockers


def test_all_required_gates_allow_domain_coding() -> None:
    gates = {
        gate: GateResult(gate, GateStatus.PASS) for gate in REQUIRED_CODING_GATES
    }

    assert coding_allowed(gates, "ticket-create") == (True, ())


def test_unit_only_evidence_does_not_allow_deployment() -> None:
    evidence = complete_release_evidence()
    not_run = SuiteResult(True, "not_run", evidence.candidate, "")
    evidence = replace(
        evidence,
        ci_integration=not_run,
        ci_contract=not_run,
        ci_regression=not_run,
        security=not_run,
        prepromotion_smoke=not_run,
    )

    eligible, blockers = deployment_eligibility(evidence)

    assert not eligible
    assert set(blockers) >= {
        "ci_integration",
        "ci_contract",
        "ci_regression",
        "security",
        "prepromotion_smoke",
    }


@pytest.mark.parametrize(
    "suite_name",
    [
        "local_relevant_checks",
        "ci_unit",
        "ci_integration",
        "ci_contract",
        "ci_regression",
        "model_quality",
        "security",
        "prepromotion_smoke",
    ],
)
@pytest.mark.parametrize("outcome", ["failed", "skipped", "missing"])
def test_failed_skipped_or_missing_applicable_suite_blocks_deployment(
    suite_name: str, outcome: str
) -> None:
    evidence = complete_release_evidence()
    broken = SuiteResult(True, outcome, evidence.candidate, "run://broken")

    eligible, blockers = deployment_eligibility(
        replace(evidence, **{suite_name: broken})
    )

    assert not eligible
    assert suite_name in blockers


def test_not_applicable_suite_requires_recorded_reason() -> None:
    evidence = complete_release_evidence()

    eligible, blockers = deployment_eligibility(
        replace(evidence, model_quality=not_applicable(""))
    )

    assert not eligible
    assert "model_quality" in blockers


def test_stale_suite_from_another_candidate_blocks_deployment() -> None:
    evidence = complete_release_evidence()

    eligible, blockers = deployment_eligibility(
        replace(evidence, ci_unit=passed("older-candidate"))
    )

    assert not eligible
    assert "ci_unit" in blockers


@pytest.mark.parametrize("field_name", ["candidate", "source_revision", "artifact_digest"])
def test_missing_candidate_identity_blocks_deployment(field_name: str) -> None:
    evidence = replace(complete_release_evidence(), **{field_name: ""})

    eligible, blockers = deployment_eligibility(evidence)

    assert not eligible
    assert "candidate_identity" in blockers


@pytest.mark.parametrize("field_name", ["rollback_ready", "monitoring_ready"])
def test_recovery_or_monitoring_gap_blocks_deployment(field_name: str) -> None:
    evidence = replace(complete_release_evidence(), **{field_name: False})

    eligible, blockers = deployment_eligibility(evidence)

    assert not eligible
    assert field_name in blockers


def test_complete_exact_candidate_evidence_allows_deployment() -> None:
    assert deployment_eligibility(complete_release_evidence()) == (True, ())


def test_postdeployment_smoke_is_required_for_production_verification() -> None:
    evidence = replace(
        complete_release_evidence(),
        postdeployment_smoke=SuiteResult(True, "not_run", "candidate-1", ""),
    )

    assert deployment_eligibility(evidence) == (True, ())
    verified, blockers = production_verification(evidence)
    assert not verified
    assert blockers == ("postdeployment_smoke",)


def test_complete_evidence_verifies_production() -> None:
    assert production_verification(complete_release_evidence()) == (True, ())


def test_backend_ai_ticket_routing_lifecycle_blocks_then_advances() -> None:
    coverage = complete_srs_coverage()
    for unanswered in (
        "actors_authority",
        "timeout_dependency_failure",
        "duplicate_idempotency",
        "partial_failure_recovery",
        "states_terminal_outcomes",
        "input_contracts",
        "output_side_effect_contracts",
        "data_lifecycle_privacy",
        "nonfunctional_requirements",
        "acceptance_oracles",
        "ownership_operations",
    ):
        del coverage[unanswered]

    blocked_g1 = assess_srs_gate(
        coverage,
        critical_open_questions=("Q-model-fallback", "Q-routing-owner"),
    )
    assert blocked_g1.status is GateStatus.BLOCKED
    assert not coding_allowed(
        {
            "G1_SRS_LOGIC": blocked_g1,
            "G2_ARCHITECTURE_CONTRACTS": GateResult(
                "G2_ARCHITECTURE_CONTRACTS", GateStatus.BLOCKED
            ),
            "G3_PLAN_TEST_STRATEGY": GateResult(
                "G3_PLAN_TEST_STRATEGY", GateStatus.BLOCKED
            ),
        },
        "ticket-routing-api",
    )[0]

    accepted_gates = {
        "G1_SRS_LOGIC": assess_srs_gate(complete_srs_coverage()),
        "G2_ARCHITECTURE_CONTRACTS": GateResult(
            "G2_ARCHITECTURE_CONTRACTS", GateStatus.PASS
        ),
        "G3_PLAN_TEST_STRATEGY": GateResult(
            "G3_PLAN_TEST_STRATEGY", GateStatus.PASS
        ),
    }
    assert coding_allowed(accepted_gates, "ticket-routing-api") == (True, ())

    full_evidence = complete_release_evidence("ticket-router-v1")
    unit_only = replace(
        full_evidence,
        ci_integration=SuiteResult(True, "not_run", "ticket-router-v1", ""),
        ci_contract=SuiteResult(True, "not_run", "ticket-router-v1", ""),
        ci_regression=SuiteResult(True, "not_run", "ticket-router-v1", ""),
        security=SuiteResult(True, "not_run", "ticket-router-v1", ""),
        prepromotion_smoke=SuiteResult(True, "not_run", "ticket-router-v1", ""),
    )
    assert not deployment_eligibility(unit_only)[0]
    assert deployment_eligibility(full_evidence) == (True, ())
    assert production_verification(full_evidence) == (True, ())


def test_skill_discovery_accepts_purpose_specific_resource_names(tmp_path) -> None:
    skill = tmp_path / "portable-name"
    (skill / "agents").mkdir(parents=True)
    (skill / "references").mkdir()
    (skill / "assets").mkdir()
    (skill / "agents" / "openai.yaml").write_text("interface: {}\n")
    (skill / "references" / "domain-checks.md").write_text("# Checks\n")
    (skill / "assets" / "delivery-record.md").write_text("# Record\n")
    (skill / "SKILL.md").write_text(
        "---\nname: example-skill\ndescription: Example.\n---\n"
        "Read [checks](references/domain-checks.md) and use "
        "[record](assets/delivery-record.md).\n"
    )
    result = RepositoryValidation()

    skills = discover_skills(tmp_path, result)

    assert skills == {"example-skill": skill}
    assert result.errors == []


def test_skill_discovery_reports_missing_metadata_and_broken_links(tmp_path) -> None:
    skill = tmp_path / "portable-name"
    skill.mkdir()
    (skill / "SKILL.md").write_text(
        "---\nname: example-skill\ndescription: Example.\n---\n"
        "Read [missing](references/missing.md).\n"
    )
    result = RepositoryValidation()

    discover_skills(tmp_path, result)

    assert "example-skill: missing agents/openai.yaml" in result.errors
    assert "example-skill: broken resource link references/missing.md" in result.errors
