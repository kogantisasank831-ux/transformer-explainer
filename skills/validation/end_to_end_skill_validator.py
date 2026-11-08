from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Iterable, Mapping


class GateStatus(str, Enum):
    PASS = "PASS"
    CONDITIONAL = "CONDITIONAL"
    BLOCKED = "BLOCKED"
    NOT_APPLICABLE = "NOT_APPLICABLE"


@dataclass(frozen=True)
class GateResult:
    gate_id: str
    status: GateStatus
    blockers: tuple[str, ...] = ()
    evidence: tuple[str, ...] = ()
    allowed_slices: frozenset[str] = frozenset()

    def permits(self, slice_id: str) -> bool:
        if self.status is GateStatus.PASS:
            return True
        return self.status is GateStatus.CONDITIONAL and slice_id in self.allowed_slices


@dataclass(frozen=True)
class CoverageItem:
    state: str
    evidence_or_reason: str

    def satisfied(self, *, core: bool) -> bool:
        if self.state == "covered":
            return bool(self.evidence_or_reason)
        if self.state == "not_applicable":
            return not core and bool(self.evidence_or_reason)
        return False


SRS_COVERAGE = (
    "objective_scope",
    "actors_authority",
    "trigger_preconditions",
    "happy_path",
    "alternate_paths",
    "invalid_missing_input",
    "unauthorized_forbidden",
    "no_result_empty_state",
    "timeout_dependency_failure",
    "duplicate_idempotency",
    "cancellation_expiry",
    "partial_failure_recovery",
    "concurrency_ordering",
    "states_terminal_outcomes",
    "input_contracts",
    "output_side_effect_contracts",
    "data_lifecycle_privacy",
    "nonfunctional_requirements",
    "acceptance_oracles",
    "ownership_operations",
)

CORE_SRS_COVERAGE = {
    "objective_scope",
    "actors_authority",
    "trigger_preconditions",
    "happy_path",
    "states_terminal_outcomes",
    "input_contracts",
    "output_side_effect_contracts",
    "acceptance_oracles",
}


def assess_srs_gate(
    coverage: Mapping[str, CoverageItem],
    *,
    critical_open_questions: Iterable[str] = (),
    ready_slices: Iterable[str] = (),
) -> GateResult:
    blockers: list[str] = []
    evidence: list[str] = []
    for area in SRS_COVERAGE:
        item = coverage.get(area)
        if item is None or not item.satisfied(core=area in CORE_SRS_COVERAGE):
            blockers.append("coverage:" + area)
        elif item.state == "covered":
            evidence.append(area + ":" + item.evidence_or_reason)
    blockers.extend("question:" + question for question in critical_open_questions)
    allowed = frozenset(ready_slices)
    if not blockers:
        return GateResult("G1_SRS_LOGIC", GateStatus.PASS, evidence=tuple(evidence))
    if allowed:
        return GateResult(
            "G1_SRS_LOGIC",
            GateStatus.CONDITIONAL,
            blockers=tuple(blockers),
            evidence=tuple(evidence),
            allowed_slices=allowed,
        )
    return GateResult("G1_SRS_LOGIC", GateStatus.BLOCKED, blockers=tuple(blockers), evidence=tuple(evidence))


REQUIRED_CODING_GATES = ("G1_SRS_LOGIC", "G2_ARCHITECTURE_CONTRACTS", "G3_PLAN_TEST_STRATEGY")


def coding_allowed(gates: Mapping[str, GateResult], slice_id: str) -> tuple[bool, tuple[str, ...]]:
    blockers: list[str] = []
    for gate_id in REQUIRED_CODING_GATES:
        gate = gates.get(gate_id)
        if gate is None:
            blockers.append(gate_id + ":missing")
        elif not gate.permits(slice_id):
            blockers.append(gate_id + ":" + gate.status.value)
    return not blockers, tuple(blockers)


@dataclass(frozen=True)
class SuiteResult:
    applicable: bool
    outcome: str
    candidate: str
    evidence: str = ""

    def passed_for(self, candidate: str) -> bool:
        if not self.applicable:
            return bool(self.evidence)
        return self.outcome == "passed" and self.candidate == candidate and bool(self.evidence)


@dataclass(frozen=True)
class ReleaseEvidence:
    candidate: str
    source_revision: str
    artifact_digest: str
    local_relevant_checks: SuiteResult
    ci_unit: SuiteResult
    ci_integration: SuiteResult
    ci_contract: SuiteResult
    ci_regression: SuiteResult
    model_quality: SuiteResult
    security: SuiteResult
    prepromotion_smoke: SuiteResult
    postdeployment_smoke: SuiteResult
    rollback_ready: bool
    monitoring_ready: bool


def deployment_eligibility(evidence: ReleaseEvidence) -> tuple[bool, tuple[str, ...]]:
    blockers: list[str] = []
    if not evidence.candidate or not evidence.source_revision or not evidence.artifact_digest:
        blockers.append("candidate_identity")
    suites = {
        "local_relevant_checks": evidence.local_relevant_checks,
        "ci_unit": evidence.ci_unit,
        "ci_integration": evidence.ci_integration,
        "ci_contract": evidence.ci_contract,
        "ci_regression": evidence.ci_regression,
        "model_quality": evidence.model_quality,
        "security": evidence.security,
        "prepromotion_smoke": evidence.prepromotion_smoke,
    }
    blockers.extend(name for name, result in suites.items() if not result.passed_for(evidence.candidate))
    if not evidence.rollback_ready:
        blockers.append("rollback_ready")
    if not evidence.monitoring_ready:
        blockers.append("monitoring_ready")
    return not blockers, tuple(blockers)


def production_verification(evidence: ReleaseEvidence) -> tuple[bool, tuple[str, ...]]:
    eligible, blockers = deployment_eligibility(evidence)
    final = list(blockers)
    if not evidence.postdeployment_smoke.passed_for(evidence.candidate):
        final.append("postdeployment_smoke")
    return eligible and not final, tuple(final)


REQUIRED_LIFECYCLE_SKILLS = {
    "ds-requirements-analysis",
    "ds-srs-gap-analysis-business-process-validation",
    "ds-repository-assessment",
    "ds-system-architecture",
    "ds-nonfunctional-requirements",
    "ds-api-contract-design",
    "ds-threat-modeling",
    "ds-implementation-planning",
    "ds-project-setup",
    "ds-production-coding-practices",
    "ds-unit-test-creation",
    "ds-integration-testing",
    "ds-contract-testing",
    "ds-regression-testing",
    "ds-test-strategy",
    "ds-ci-pipeline-engineering",
    "ds-production-readiness-review",
    "ds-smoke-release-verification",
    "ds-deployment-execution",
    "ds-ai-production-monitoring",
}


@dataclass
class RepositoryValidation:
    errors: list[str] = field(default_factory=list)
    observations: list[str] = field(default_factory=list)
    skill_names: set[str] = field(default_factory=set)

    @property
    def valid(self) -> bool:
        return not self.errors


def _frontmatter_name(skill_file: Path) -> str | None:
    match = re.search(r"(?m)^name:\s*([a-z0-9-]+)\s*$", skill_file.read_text())
    return match.group(1) if match else None


def discover_skills(skills_root: Path, result: RepositoryValidation) -> dict[str, Path]:
    discovered: dict[str, Path] = {}
    for skill_file in skills_root.glob("*/SKILL.md"):
        name = _frontmatter_name(skill_file)
        if not name:
            result.errors.append("missing frontmatter name: " + str(skill_file))
            continue
        if name in discovered:
            result.errors.append("duplicate skill name: " + name)
            continue
        discovered[name] = skill_file.parent
        if not (skill_file.parent / "agents/openai.yaml").is_file():
            result.errors.append(f"{name}: missing agents/openai.yaml")
        text = skill_file.read_text()
        for link in re.findall(r"\[[^]]+\]\(([^)]+)\)", text):
            target = link.strip().strip("<>").split("#", 1)[0]
            if not target or re.match(r"^[a-z][a-z0-9+.-]*:", target):
                continue
            if not (skill_file.parent / target).is_file():
                result.errors.append(f"{name}: broken resource link {target}")
    result.skill_names = set(discovered)
    return discovered


def validate_repository(repo_root: Path, skills_root: Path | None = None) -> RepositoryValidation:
    result = RepositoryValidation()
    skills_root = skills_root or repo_root / "skills"
    skills = discover_skills(skills_root, result)
    if len(skills) != 91:
        result.errors.append(f"expected 91 skills, found {len(skills)}")
    missing = REQUIRED_LIFECYCLE_SKILLS - set(skills)
    result.errors.extend("missing lifecycle skill: " + name for name in sorted(missing))

    required_docs = {
        "AGENTS.md": ["End-to-end delivery gates", "G1", "G5"],
        "CLAUDE.md": ["END_TO_END_PROJECT_LIFECYCLE.md", "affected slice"],
        "PROJECT_LOGIC.md": ["TOOLKIT-030"],
        "skills/templates/PROJECT_LOGIC.md": ["Delivery stage gates", "G1_SRS_LOGIC"],
        "skills/templates/WORK_PROGRESS.md": ["Current delivery gate"],
        "docs/END_TO_END_PROJECT_LIFECYCLE.md": ["G1 — SRS", "G5 — Exact-candidate verification"],
    }
    for relative, markers in required_docs.items():
        path = repo_root / relative
        if not path.is_file():
            result.errors.append("missing document: " + relative)
            continue
        text = path.read_text()
        for marker in markers:
            if marker not in text:
                result.errors.append(f"{relative}: missing marker {marker}")

    skill_markers = {
        "ds-srs-gap-analysis-business-process-validation": ["G1_SRS_LOGIC", "coding readiness"],
        "ds-implementation-planning": ["G3_PLAN_TEST_STRATEGY", "WORK_PROGRESS.md"],
        "ds-production-coding-practices": ["G1_SRS_LOGIC", "G2_ARCHITECTURE_CONTRACTS", "G3_PLAN_TEST_STRATEGY"],
        "ds-project-setup": ["domain behavior", "G1_SRS_LOGIC"],
        "ds-production-readiness-review": ["G5_EXACT_CANDIDATE", "UNKNOWN/FAIL"],
    }
    for name, markers in skill_markers.items():
        directory = skills.get(name)
        if not directory:
            continue
        text = (directory / "SKILL.md").read_text()
        for marker in markers:
            if marker not in text:
                result.errors.append(f"{name}: missing lifecycle marker {marker}")

    result.observations.append(f"skills={len(skills)}")
    result.observations.append(f"lifecycle_skills={len(REQUIRED_LIFECYCLE_SKILLS - missing)}")
    return result


def _cli() -> int:
    parser = argparse.ArgumentParser(description="Validate the 91-skill end-to-end delivery lifecycle")
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--skills-root", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = validate_repository(args.repo_root, args.skills_root)
    payload = {
        "valid": result.valid,
        "errors": result.errors,
        "observations": result.observations,
        "skill_count": len(result.skill_names),
    }
    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print("PASS" if result.valid else "FAIL", *result.observations)
        for error in result.errors:
            print("-", error)
    return 0 if result.valid else 1


if __name__ == "__main__":
    raise SystemExit(_cli())
