# Modality

This repository is reserved for reusable, non-authoritative contracts for
opaque signal/effect transduction. It does not own Organism interpretation,
body state, environmental phenomena, or persistent modality state.

No concrete numeric transduction operators, default modality catalogue, units,
or temporal model are currently ratified for TARGET. In their absence, callers
must preserve an opaque signal unchanged rather than assign it an inherited
numeric meaning. A future operator requires a target consumer and an explicit
contract for input/output semantics, state ownership, initialization, update
rule, range, saturation, time basis, determinism, and configuration.

Historical `SensorySystem`, plasticity, predictive-credit, and interoception
code remains outside this package; see [`MIGRATION.md`](MIGRATION.md) for
source provenance and disposition.

## Development

```sh
python -m pip install -e '.[test]'
python -m pytest
```

## Status

This is a migration-stage target repository, not a declaration of cut-over or
compatibility with the historical source. See [`MIGRATION.md`](MIGRATION.md)
for exact source provenance and current dispositions.
