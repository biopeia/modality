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

## Follow-up source inventory — 2026-10-09

Re-audited the complete pinned `symbiont/src/symbiont/sensory/` package and
`symbiont/tests/unit/sensory/` at source SHA
`80d372a186513035f85a769db886e505cabba52d`. This is a disposition inventory,
not authorization to move stateful behavior into Modality. The source remains
unchanged. A source file's presence in this inventory does not imply it is
complete or portable as a whole.

| Source path (pinned SHA) | Target disposition / destination | Boundary and validation caveat |
|---|---|---|
| `symbiont/src/symbiont/sensory/transduction.py` | `MOVE` to this package (already copied) | Stateless bounded operators are reusable capability behavior; no claim about biological validity. Existing `tests/test_transduction.py` covers the extracted operators. |
| `symbiont/src/symbiont/sensory/modalities.py` | `SPLIT`; reusable `SensoryModality` descriptor/default catalog copied here; remaining references stay with Organism | Descriptor is capability metadata only; it does not own or define semantic interpretation. Existing `tests/test_modalities.py` covers the copied descriptor. |
| `symbiont/src/symbiont/sensory/evidence.py` | `SPLIT`; `EvidenceCount`/`SampleCount` belongs to Organism and has migrated to `organism.foundation.evidence` (see Organism migration record); no Modality destination | Count type is not a modality, physical time, scheduler, or evidence authority. Sensory-specific estimator/credit behavior remains Organism-owned. |
| `symbiont/src/symbiont/sensory/sensor.py` | `DEFER` to Organism | `SensorState` holds durable phenotype, identity, learning/utility summaries, and temporal continuation state. Moving it to a capability library would transfer semantic authority and continuity ownership. |
| `symbiont/src/symbiont/sensory/system.py` | `DEFER` to Organism; later `SPLIT` only if a concrete owner boundary is established | Orchestrates organism sensor lifecycle, learning, plasticity, selection, and checkpoint state while consuming host readings. Its current aggregate API is not a neutral Modality executor. |
| `symbiont/src/symbiont/sensory/plasticity.py` | `DEFER` to Organism | Mutation records and development rules alter Organism-owned phenotype; no independent capability-only behavior identified. |
| `symbiont/src/symbiont/sensory/predictive_credit.py` | `DEFER` to Organism | Online predictive evidence and selection credits affect Organism learning/selection and have explicit replay/checkpoint handling. |
| `symbiont/src/symbiont/sensory/fitness.py` | `DEFER` to Organism | Fitness inputs encode organism-side learning/selection semantics; moving formulas would make Modality an authority over utility. |
| `symbiont/src/symbiont/sensory/limits.py` | `DEFER` to Organism | Bounds cover sensor counts, mutations, temporal depth, and organism sensory checkpoint size, not a generic transduction capability. |
| `symbiont/src/symbiont/sensory/checkpoint.py` | `DEFER` to Organism | Serializes/restores `SensorySystem`; checkpoint compatibility is coupled to Organism-owned state and recovery behavior. |
| `symbiont/src/symbiont/sensory/interoception.py` | `SPLIT` candidate, deferred pending explicit contracts: physiological channels/state to Embodiment and Organism-facing projection to their owner boundary; host sampling/telemetry observation to host/Observation or Lab apparatus | The current provider combines somatic values, organism-facing cognitive signals, host capability discovery, monotonic timestamps, and host telemetry. No partial code extraction is safe without defining those interfaces and ownership. |
| `symbiont/src/symbiont/sensory/__init__.py` | `SPLIT` as exports follow each moved owner; do not copy package-wide facade | The source facade re-exports both the already extracted capability pieces and deferred Organism-owned state. |
| `symbiont/tests/unit/sensory/test_system.py`, `test_fitness.py`, `test_selection.py` | `SPLIT`/`DEFER` with their Organism-owned implementation | These tests assert development, utility, learning, checkpoint, and selection semantics, not a standalone Modality contract. The Modality suite retains focused tests for copied pure behavior. |
| `symbiont/tests/unit/sensory/test_interoception.py`, `test_interoception_independence.py`, `test_interoception_is_intrinsic.py`, `fake_telemetry.py` | `DEFER` with the interoception ownership split | Tests exercise host instrumentation, somatic refresh, privacy, and organism-facing projection together; extracting a subset now could falsely validate an unresolved boundary. |
| `symbiont/tests/unit/sensory/README.md`, `__init__.py` | `DEFER` with source test package | Source test instructions/package markers are not reusable runtime capability. Recreate only focused tests alongside any later authorized extraction. |

### Result and next Modality work

This audit found no additional bounded source-code slice that can move into
Modality without either duplicating an existing extraction or choosing an
unresolved semantic owner. In particular, do not move `SensorState`, its
selection/fitness/plasticity pipeline, or `InteroceptionProvider` merely to add
code to this repository. The next code-bearing step is to define and verify the
necessary Organism/Embodiment/Observation contracts for interoceptive inputs;
that work must be led at those owner boundaries. Meanwhile, keep this package's
pure transduction tests and build validation independent. This conclusion is
limited to the pinned sensory package inventory; it does not prove that
independent Modality versioning is permanently justified or that the Modality
repository is complete.
