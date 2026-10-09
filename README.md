# Modality contracts

This repository contains a small, reusable contract/library slice for bounded sensory transduction. It is not a semantic authority and does not own Organism interpretation, body state, or environmental phenomena.

The initial extraction provides:

- `TransductionKind` and `apply_transduction`, a bounded deterministic primitive set.
- `SensoryModality`, a validated capability descriptor and the existing default descriptors.

Dynamic state is not assigned to this library by default. The CURRENT `SensorState` and its temporal/evidence state remain an Organism-owned candidate; episode calibration may be Embodiment-owned. The old `SensorySystem`, plasticity, predictive credit, and interoception code are intentionally deferred because they mix Organism learning/state or depend on host/body contracts.

## Development

```sh
python -m pip install -e '.[test]'
python -m pytest
```

## Status

This is a reversible copy-first migration slice from the pinned source snapshot. See [`MIGRATION.md`](MIGRATION.md) for exact provenance and dispositions. It does not declare a migration cut-over or final API.
