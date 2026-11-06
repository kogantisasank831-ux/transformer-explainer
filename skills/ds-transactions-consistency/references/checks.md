# Transaction and consistency checks

- Name the invariant, writers, records/resources, commit point, and observable failure. Map every implicit/autocommit boundary.
- Verify engine/version isolation semantics, statement snapshots, predicate/range locks, constraint timing, replica reads, ORM flush behavior, and error codes.
- Prefer unique/check/foreign-key/exclusion constraints and conditional updates for local invariants. Authorization remains separate.
- For locks, define acquisition order, timeout, lease/ownership, cancellation, deadlock behavior, and crash recovery. Do not hold locks across unbounded calls.
- Retry the whole transaction only for documented transient failures; reset the session and bound attempts. Test duplicate side effects and ambiguous commit outcomes.
- For outbox/inbox or saga flows, define atomic write, publisher acknowledgement, dedupe key, ordering scope, replay, poison handling, compensation, and reconciliation.
- Test real concurrent interleavings and verify final invariants. Sequential unit tests are insufficient evidence for race safety.

Consult official documentation for the selected engine/version. PostgreSQL users should review [transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html) and application-level consistency guidance.
