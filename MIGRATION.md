# Migration record

## Source provenance

- Source repository: `https://github.com/biopeia/symbiont-lab` (local source checkout; repository name at extraction: `symbiont-lab`).
- Source SHA: `80d372a186513035f85a769db886e505cabba52d`.
- Audit baseline: `cef998a55aae32ed8b2f7373079c11667b01e915`.
- Source package root: `symbiont/src/symbiont/sensory/`.
- Source commits: snapshot commit above; no separate historical path-extraction commit was used.

## Dispositions

| Source path | Destination | Disposition | Notes |
|---|---|---|---|
| `symbiont/src/symbiont/sensory/transduction.py` | `src/modality/transduction.py` | `MOVE` (copy-first) | Pure bounded deterministic operators; no persistent owner state. |
| `symbiont/src/symbiont/sensory/modalities.py` | `src/modality/modalities.py` | `SPLIT` (copy-first) | Reusable descriptor/default capability catalog extracted; descriptors do not confer semantic authority. |
| `symbiont/tests/unit/sensory/test_system.py` | — | `DEFER` | Exercises Organism-owned sensory system, learning, and state lifecycle; not a focused library test. |
| `sensory/system.py`, `sensor.py`, `plasticity.py`, `predictive_credit.py`, `fitness.py`, `checkpoint.py` | — | `DEFER` | Organism-owned learned/temporal state and developmental behavior; not moved into Modality. |
| `sensory/interoception.py` | — | `DEFER` | Depends on host reading/capability contracts and somatic/Organism signals; requires boundary mapping. |

No source files were removed or changed. The copied modules are unmodified apart from package-relative import paths already being local to the new package. No historical Git path extraction was attempted because this target is a deliberately bounded recomposition rather than a clean whole-directory move.

## Dynamic state ownership notes

- Transduction function arguments/results are call-local; no persistent modality state is created.
- The source `SensorState` temporal state (previous input, integrator, outputs, developmental counters) is deferred and is not owned by this repo in this slice. Organism/Embodiment allocation needs explicit contract reconciliation.
- Any pure scratch state in a future transduction executor should remain implementation-local and non-authoritative unless evidence demonstrates otherwise.

## Validation

Validation outcomes are recorded with the migration commit/PR. This initial slice is not a final target API or architectural cut-over.
