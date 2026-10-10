# Modality

This repository is reserved for reusable, non-authoritative contracts for
opaque signal/effect transduction. It does not own Organism interpretation,
body state, environmental phenomena, or persistent modality state.

The first-sensor fixture has one explicitly revisioned, stateless identity
mapping for a dimensionless scalar field in `[0, 1]`. It rejects invalid or
out-of-range values; it does not clip, add state, or assign semantic meaning.
This narrow mapping is not a general operator catalogue or universal sensing
law. The environment phenomenon, receptor and causal provenance remain owned
by their respective domains. Other numeric transductions still require a
target consumer and an explicit contract for input/output semantics, state
ownership, initialization, update rule, range, saturation, time basis,
determinism, and configuration.

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
