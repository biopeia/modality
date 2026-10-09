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
- Persistent state encountered during migration must be assigned to exactly one of these semantic owners: `ORGANISM_OWNED`, `EMBODIMENT_OWNED`, or `ENVIRONMENT_OWNED`. Pure scratch state that does not survive a call may be `IMPLEMENTATION_EPHEMERAL`.
- The source `SensorState` temporal state (previous input, integrator, outputs, developmental counters) is deferred; its individual fields must be classified under those allowed ownership labels before any migration. `MODALITY_OWNED` is not an allowed persistent-state label absent an explicit new architecture decision.
- Any pure scratch state in a future transduction executor should remain `IMPLEMENTATION_EPHEMERAL` and non-authoritative.

## Provisional repository status

The owner has decided to keep Modality as a **provisional independent repository
during the migration**. This records a packaging/versioning decision only: it
does not grant semantic authority, persistent-state ownership, or permission to
move unresolved state into this package. Modality remains a contract/capability
library; Organism, Embodiment, Environment, and implementation-local code retain
their respective ownership boundaries.

Revisit whether an independent repository is still justified when any of these
review triggers occurs:

1. The migration is largely complete.
2. Evidence shows independent Modality versioning is unnecessary.
3. Persistent coupling demonstrates that a meaningful boundary does not exist.

Until a new explicit architecture decision changes the rule, persistent state
may be labeled only `ORGANISM_OWNED`, `EMBODIMENT_OWNED`, `ENVIRONMENT_OWNED`, or
`IMPLEMENTATION_EPHEMERAL`; do not introduce `MODALITY_OWNED`.

## Validation

Validation outcomes are recorded with the migration commit/PR. This initial slice is not a final target API or architectural cut-over.

## Complete source snapshot inventory — 2026-10-09

This inventory expands the earlier sensory-only audit to all Modality-owned
source trees visible at the pinned monorepo snapshot. “Candidate” means a
disposition proposal for migration tracking, not approval to copy legacy code.
The SHA in each provenance cell is the last path commit reachable at the pinned
source revision; the blob is the exact content object at that revision. The
snapshot SHA remains `80d372a186513035f85a769db886e505cabba52d`.

### Historical sensory implementation

The source tree is `symbiont/src/symbiont/sensory/`. The symbols listed are
top-level classes/functions; imports/constants and private helpers remain in
the source blob and should be re-audited if a future bounded extraction is
proposed.

| Source path | Path commit / blob | Top-level symbols | Candidate disposition / target | Consumer and test evidence | Reason / caveat and DEFER closure trigger |
|---|---|---|---|---|---|
| `symbiont/src/symbiont/sensory/__init__.py` | `60843cba5e66e782054da96e187ca572f0254098` / `e19ab55d8512282afbec9d4256a98423a636bd03` | package exports | `SPLIT`; no package-wide facade | sensory tests and `symbiont/src/symbiont/core/domains/perception.py` | exports mix capability contracts with Organism state. Revisit only after each symbol's owner is resolved. |
| `symbiont/src/symbiont/sensory/checkpoint.py` | `13720935595fedabec2c376dc933629b0deae5aa` / `b56459c72e5ecd1b35b93f7a92f0948c3d7c9e31` | `export_sensory_checkpoint`, `restore_sensory_checkpoint` | `DEFER` to Organism; no Modality destination | `test_system.py`, `test_selection.py`, core cognition/perception/runtime | serializes owner state and recovery semantics. Close only with Organism checkpoint contract and owner tests. |
| `symbiont/src/symbiont/sensory/evidence.py` | `0c87bb9012342a59564c97654f34eea17157ecee` / `d2bc5c9dee18e113ffbd5a1540dc200c5882f3a3` | `EvidenceCount` | `SPLIT`; Organism-side count moved under `organism.foundation.evidence` | Organism migration record; `test_selection.py`, `test_fitness.py` | count is not a Modality authority; verify downstream import consumers before removing source copy. |
| `symbiont/src/symbiont/sensory/fitness.py` | `13720935595fedabec2c376dc933629b0deae5aa` / `d4c90ff31142fc6be1244dda834252b610fb2a8f` | `sensory_fitness` | `DEFER` to Organism | `test_fitness.py`, `test_system.py`, perception studies | formula encodes learning/utility semantics. Close only at Organism boundary; do not treat as general transduction. |
| `symbiont/src/symbiont/sensory/interoception.py` | `9b8095d5f1c6248c9462c9e6fd02d2763ed76d1d` / `b4dcf5f2b60f7ca24feaf5c2fa5f95d004ea4e19` | `HostTelemetry`, `InteroceptionProvider`, `ShamInteroceptionProvider` | `DEFER` / possible `SPLIT` among Embodiment, Organism, and host/Observation | `test_interoception.py`, `test_interoception_independence.py`, `test_interoception_is_intrinsic.py`, `fake_telemetry.py`; `core/domains/physiology.py` | conflates body signals, organism projection, host capability reads, and timestamps. Close only after each owner defines and tests its boundary. |
| `symbiont/src/symbiont/sensory/limits.py` | `13720935595fedabec2c376dc933629b0deae5aa` / `9e3c2d0ab083647a499dc1bf78ad298c2b341076` | `SensoryLimits` | `DEFER` to Organism | `test_system.py`, `test_selection.py`, `test_checkpoint.py` | limits sensor count, mutation and checkpoint state; not generic capability limits. Revisit if an independently owned Modality resource limit is demonstrated. |
| `symbiont/src/symbiont/sensory/modalities.py` | `13720935595fedabec2c376dc933629b0deae5aa` / `f2f87e3c9b12442f3f9b515b4847749ade186b15` | `SensoryModality` | `SPLIT`; descriptor subset already exists in `src/modality/modalities.py` in the target repo | target `tests/test_modalities.py`; source `test_system.py`, `test_selection.py` | descriptor metadata does not confer semantic authority. Re-audit when changing descriptor contracts; never carry Organism semantics through the catalog. |
| `symbiont/src/symbiont/sensory/plasticity.py` | `13720935595fedabec2c376dc933629b0deae5aa` / `994e2ced6015a1cf05c67b9d906cad9630dba0fe` | `SensoryMutationKind`, `SensoryMutation` | `DEFER` to Organism | `test_system.py`, `test_selection.py` | development changes Organism-owned phenotype; close only with Organism development lifecycle. |
| `symbiont/src/symbiont/sensory/predictive_credit.py` | `60843cba5e66e782054da96e187ca572f0254098` / `38c30cc4b18e45fc5e178f227be254a1d05d86dd` | `PairwisePredictiveEvidence`, `SensorySelectionEngine` | `DEFER` to Organism | `test_selection.py`, `test_system.py`, core cognition credit tests | selection/credit affects Organism learning and has replay/checkpoint semantics. Close only within those owner contracts. |
| `symbiont/src/symbiont/sensory/sensor.py` | `13720935595fedabec2c376dc933629b0deae5aa` / `ce0ea82c32bea7d29d654e80094c07051c7ffc45` | `MaturityState`, `SensorState` | `DEFER` to Organism | `test_system.py`, `test_selection.py`, runtime/perception consumers | contains identity, acquired phenotype, learning summaries and temporal state. Do not put persistent state in Modality. |
| `symbiont/src/symbiont/sensory/system.py` | `6ea9d3844a8fcb1bbc0a53c48680981d72ff4085` / `ed2d4fb12f71b39e5a5ae2cbc7c0e68b82c0f395` | `SensorySystem` | `DEFER` to Organism; later split only with explicit owner contract | source sensory tests and perception/runtime consumers | orchestrates organism lifecycle, selection, plasticity and checkpoint. Not a neutral Modality executor. |
| `symbiont/src/symbiont/sensory/transduction.py` | `13720935595fedabec2c376dc933629b0deae5aa` / `40eb209ca71b1483aa52e87409aef5ee3df73686` | `TransductionKind`, `apply_transduction` | `MOVE` candidate; extracted as `src/modality/transduction.py` | target `tests/test_transduction.py`; source `test_system.py` | bounded/stateless operators only; the extraction does not establish biological validity or signal meaning. |

### Monorepo Modality package and associated tests

At the same source pin, `modality/` is also present as a separate tree. These
rows record it explicitly so the source snapshot is not mistaken for a complete
inventory merely because the extracted target initially contained only the
sensory slice. They do not authorize wholesale copying. Test rows refer to the
source test suite; destination status is evaluated against the Biopeia Modality
repo as of this PR's base commit.

| Source path | Path commit / blob | Symbols | Candidate disposition / target | Consumer or test | Reason / caveat / closure trigger |
|---|---|---|---|---|---|
| `modality/src/modality/__init__.py` | `7d090d58e214b650abcc4925d2aa27b403706314` / `7626a8c9d2ca40198ccf21a35ffe3ce8070fd3c2` | package exports | `SPLIT` / current package entry point differs | package build and imports | inventory exports individually before any copy; no blanket facade transfer. |
| `modality/src/modality/host/__init__.py` | `7a63ec3ce140514e085789f498e7c73a72eca3fc` / `3e2f765d9575bc42088a13cdbeb94f4c180413a5` | package exports | `DEFER` pending boundary review | `tests/host/*` | host APIs may expose host state; resolve authority, privacy and data provenance before adopting. |
| `modality/src/modality/host/contracts.py` | `e01b4a8412cafe34573f541c263e36af675d1b7a` / `7146a8cb1442d8c5bc7cc7ae036cbbee0613372a` | `HostDiscoveryProvider`, `HostReadingProvider`, `HostTickObserver` | `DEFER` | host tests; source host providers | no proof these interfaces match ratified domain contracts; close with owner/security review and consumer map. |
| `modality/src/modality/host/linux_surfaces.py` | `7a63ec3ce140514e085789f498e7c73a72eca3fc` / `7612329c52edf235ccdd60839d7b53942f2421ab` | `LinuxSurfaceProvider` | `DEFER` | `test_linux_surfaces.py` | platform-specific host sampling, not environment or organism truth; close after data/privacy boundary review. |
| `modality/src/modality/host/portable_surfaces.py` | `7a63ec3ce140514e085789f498e7c73a72eca3fc` / `f51452927191be2efc2f6053fcfdf3cd9a293ccf` | `_finite`, `_MemoryStatusEx`, `_SystemPowerStatus`, `PortableSurfaceProvider` | `DEFER` | `test_portable_surfaces.py` | host-specific optional readings; verify platform behavior and privacy semantics before adoption. |
| `modality/src/modality/host/process_telemetry.py` | `7a63ec3ce140514e085789f498e7c73a72eca3fc` / `7cf30d4f22da2f5e8ec7ff8c605451130fbdbee7` | `HostProcessTelemetry` | `DEFER` | `test_process_telemetry.py`; Lab/runtime telemetry consumers | process metrics are host observations, not Organism semantic claims; close with source/producer/provenance contract. |
| `modality/src/modality/host/records.py` | `7a63ec3ce140514e085789f498e7c73a72eca3fc` / `6e412bb2523df89b91e1625da717127f1a200dbc` | `CapabilityKind`, `Unit`, `ReadingQuality`, `ReadingPrivacyClass`, `Capability`, `SensorReading` | `DEFER` | host tests and provider implementations | candidate record semantics require review for explicit units, epistemic status, subject identity and authority; do not silently freeze schema. |
| `modality/src/modality/host/stdlib.py` | `7a63ec3ce140514e085789f498e7c73a72eca3fc` / `61d9cad1b62013695ec794d1b439c343e0aecf1b` | `StandardLibraryProvider`, `_disk_usage_total` | `DEFER` | host tests/provider composition | optional host measurements; not a generic physical environment model. |
| `modality/src/modality/host/stdlib_readings.py` | `7a63ec3ce140514e085789f498e7c73a72eca3fc` / `0462d6bd3a2bb2c30acefdfa76bdcc460608a794` | `StandardLibraryReadingProvider` | `DEFER` | host tests; provider consumers | same unresolved host-readings boundary; close with explicit inclusion/exclusion and owner contract. |
| `modality/src/modality/vision.py` | `0f75c709bba8bfc9505a769662e9bf0e8e7e074a` / `2aaef3b63413df76256279c52284d7c617e08723` | `PerceptualTopology`, `_sphere`, `_tube`, `_nearest`, `_intersect`, `VisualApparatus` | `DEFER` pending Embodiment/Environment/Observation family contracts | `test_vision_ray_caster.py`; Lab physics3d apparatus/workbench consumers | geometry and visual sampling are apparatus behavior; do not give Modality ground-truth authority or define Observation wire semantics here. Close after modality/owner contracts and consumers are reviewed. |
| `modality/README.md` | `7a63ec3ce140514e085789f498e7c73a72eca3fc` / `b7acd999b6ff2b4cb914df06cd6edb82a5ead463` | package documentation | `DEFER` as source documentation; revalidate claims against target contracts | human/package users | documentation is not a code consumer; do not assume target policy merely from this historical README. |
| `modality/pyproject.toml` | `0f75c709bba8bfc9505a769662e9bf0e8e7e074a` / `0be64127d27f3a6cb8d2f604987f7cacad512775` | package/build metadata | `REWRITE` for target packaging, not copy | target package build | build metadata is repo-specific and must not be moved verbatim; target `pyproject.toml` is authoritative for current build. |
| `modality/tests/__init__.py` | `282c44eea894faedb57763c3545a1401cf032a86` / `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` | none | `DROP` as source artifact; recreate local test package only if needed | source suite | empty package marker has no runtime semantics. |
| `modality/tests/host/__init__.py` | `7a63ec3ce140514e085789f498e7c73a72eca3fc` / `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` | none | `DROP` as source artifact | host suite | empty marker only. |
| `modality/tests/host/test_linux_surfaces.py` | `7a63ec3ce140514e085789f498e7c73a72eca3fc` / `3d49e1fbc09a585018b471f1d6cc8ffc764b1858` | `_provider_over`, nine `test_*` functions | `DEFER` with implementation | `LinuxSurfaceProvider` | tests pin platform/filter/privacy behavior; re-author only after adopting reviewed contract. |
| `modality/tests/host/test_portable_surfaces.py` | `7a63ec3ce140514e085789f498e7c73a72eca3fc` / `009b2803b50739db4054b8a325b110f748eff21e` | three `test_*` functions | `DEFER` with implementation | `PortableSurfaceProvider` | platform-specific behavior, not portable semantic authority. |
| `modality/tests/host/test_process_telemetry.py` | `7a63ec3ce140514e085789f498e7c73a72eca3fc` / `0011e50914b73011c2ba501782bc2d07b1af4833` | three `test_*` functions | `DEFER` with implementation | `HostProcessTelemetry` | verifies host telemetry only; no evidence of scientific/biological meaning. |
| `modality/tests/test_self_contained.py` | `792d2dbd3e507d1d41300456cf826d8efe19fddb` / `e96cea3d3d31d23dd031fdb09a208c32ff9fa3b2` | `test_no_other_domain_is_installed_or_loaded`, `test_receptor_adjacency_is_over_opaque_ids_only` | `MOVE` candidate as target package-boundary tests | package installation | useful target isolation assertions; run against target layout rather than treating source test as proof of runtime behavior. |
| `modality/tests/test_vision_ray_caster.py` | `0f75c709bba8bfc9505a769662e9bf0e8e7e074a` / `f3e337ee2b63c908f44b73560255ec779d59c974` | `_sample`, five `test_*` functions | `DEFER` with vision boundary | `VisualApparatus` | tests preserve implementation behavior but cannot ratify modality ownership or physical calibration. |
| `modality/tests/README.md` | `282c44eea894faedb57763c3545a1401cf032a86` / `aa382f367e001ee4ea564df5889b0d7ab2da31bc` | test documentation | `DROP` as source artifact | none | source-local guidance is not target evidence; write target-specific docs if needed. |
| `modality/tests/host/README.md` | `7a63ec3ce140514e085789f498e7c73a72eca3fc` / `246c7324ef2d848d0ee46e4a46e8921e7ffc67ca` | host test documentation | `DROP` as source artifact | none | same; no runtime contract. |

### Historical sensory test modules

Each path below is source evidence, not a mandate to preserve every assertion.
The current target keeps focused local tests for the extracted operators and
descriptors; owner-specific tests remain with their owning domain. Blob and
path-commit data are exact at the pinned snapshot.

| Source path | Path commit / blob | Covered symbols / role | Candidate disposition | Consumers / caveat |
|---|---|---|---|---|
| `symbiont/tests/unit/sensory/__init__.py` | `282c44eea894faedb57763c3545a1401cf032a86` / `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` | empty package marker | `DROP` | no test semantics. |
| `.../fake_telemetry.py` | `7a63ec3ce140514e085789f498e7c73a72eca3fc` / `07f4db6867dc79611554b4806d70bbd115e978c9` | `FakeTelemetry` | `DEFER` with interoception tests | test fixture couples source tests to host telemetry API; recreate only under tested owner contracts. |
| `symbiont/tests/unit/sensory/test_fitness.py` | `282c44eea894faedb57763c3545a1401cf032a86` / `738db038f4e60c4675313aa09e1b56799c50b02d` | `test_health_and_novelty_cannot_create_utility_without_downstream_gain`; `test_demonstrated_gain_is_modulated_by_quality_and_cost` | `DEFER` to Organism | assertions exercise utility/learning semantics. |
| `symbiont/tests/unit/sensory/test_interoception.py` | `9b8095d5f1c6248c9462c9e6fd02d2763ed76d1d` / `ab5cffae0fe86cb717d97d9398bf75ab5ccebcb0` | `_provider`; `test_interoception_provider_discovery`; `test_interoception_provider_sampling_and_update`; `test_interoception_organism_projection_is_bounded_and_uses_ratio_units`; `test_sham_interoception_preserves_manifest_but_projects_neutral_values`; `test_interoception_action_pressure_includes_integrity_and_repair_channels`; `test_interoception_physiological_refresh_does_not_reset_computational_channels`; `test_host_telemetry_is_not_published_as_an_organism_measurement`; `test_without_host_telemetry_only_the_organism_channels_exist`; `test_host_telemetry_is_published_under_the_persisted_interoception_source` | `DEFER` pending split | combined tests must be divided by body-state, observation, host instrumentation and Organism projection owners. |
| `symbiont/tests/unit/sensory/test_interoception_independence.py` | `1da18162b7dd3cf9b6da0884c75e14f7706856cc` / `78f59dfb6464ab8a8899a0c43dc145773ba2b643` | `_intrinsic`; `test_replacing_host_telemetry_leaves_intrinsic_state_unchanged`; `test_removing_host_telemetry_leaves_intrinsic_state_unchanged`; `test_without_host_telemetry_the_organism_publishes_only_its_own_channels`; `test_canonical_profile_v1_is_invariant_to_unperceived_host_telemetry` | `DEFER` pending owner boundary | keep the negative guarantees when their owner tests are rebuilt; do not lose isolation assertions. |
| `symbiont/tests/unit/sensory/test_interoception_is_intrinsic.py` | `174983f0c24e1ed9301fe7e1969c8252097cdc54` / `c008afeed19c073f5d38bf035bb88964d74f5fef` | `test_only_the_mode_decides`; `test_a_minimal_organism_with_interoception_senses_its_own_state` | `DEFER` to Organism/Embodiment contract | preserve claim distinction between own-state and host readings. |
| `symbiont/tests/unit/sensory/test_selection.py` | `2ae96d4735fe72d57b7f7611bb9e2c8fcf51175d` / `a69d8e812eacf0287fbfa65f3737ce11b28dbe93` | `test_pairwise_predictive_evidence_beats_persistence_for_linear_relation`; `test_selection_engine_does_not_need_an_evaluator_target_label`; `test_selection_checkpoint_excludes_previous_raw_values`; `test_selection_engine_is_bounded`; `test_independent_noise_does_not_receive_credit_for_merely_beating_persistence`; `test_same_source_predictability_is_not_selection_credit`; `test_selection_v1_checkpoint_is_rejected` | `DEFER` to Organism | not a Modality execution contract. |
| `symbiont/tests/unit/sensory/test_system.py` | `1a7b70730c2730932086c4dff7fd922fb5c8e293` / `7f9365c49c13e6533126e5c06b96c35803f85625` | `reading`; `test_identity_sensor_preserves_legacy_percept_while_owning_sensor_identity`; `test_one_source_can_produce_two_distinct_percept_streams`; `test_modalities_are_structurally_non_equivalent`; `test_multisource_sensor_combines_sources_without_creating_external_signal`; `test_checkpoint_persists_phenotype_but_not_raw_transient_values`; `test_plastic_step_can_develop_non_identity_receptor_without_target_label`; `test_parameter_adaptation_uses_local_response_dynamics_only`; `test_plastic_step_never_exceeds_mutation_window_budget`; `test_plastic_step_can_create_multisource_receptor_without_evaluator_pair`; `test_adaptive_identity_sensor_keeps_stable_organism_owned_name_when_source_alias_changes`; `test_restore_accepts_history_for_sensor_that_was_later_pruned`; `test_restore_rejects_boolean_numeric_checkpoint_fields`; `test_restore_preserves_exact_modality_constitution`; `test_downstream_utility_rewards_only_the_sensor_named_as_predictive_source`; `test_temporal_sensor_marks_exactly_first_post_restore_output_as_cold_start`; `test_germinal_copy_inherits_exact_capacity_without_acquired_phenotype`; `test_phenotype_projects_opaque_signal_lineage_for_multisource_sensor`; `test_unique_unproductive_sensor_is_pruned_only_after_evaluation_grace`; `test_modality_cannot_exceed_sensory_constitution_bounds`; `test_acquisition_cost_is_shared_across_receptors_using_same_source`; `test_multisource_acquisition_cost_sums_allocated_source_shares`; `test_known_source_without_raw_sample_does_not_fabricate_sensor`; `test_v1_sensory_checkpoint_is_rejected`; `test_sensory_selection_checkpoint_contains_no_raw_previous_percept_value`; `test_phenotype_view_exposes_current_substrate_without_source_semantics`; `test_capacity_pressure_skips_new_identity_source_without_terminating`; `test_plastic_step_does_not_overflow_full_sensor_capacity`; `test_capacity_rejections_are_checkpointed_as_bounded_aggregate` | `SPLIT`/`DEFER` to Organism | retain owner-side invariants; no bulk copying into Modality. |
| `symbiont/tests/unit/sensory/README.md` | `282c44eea894faedb57763c3545a1401cf032a86` / `fb247cabade8a70a3ae75f18fba2fd4c2d60b5f9` | source test instructions | `DROP` as source artifact | rewrite only if target-specific test instructions are needed. |

### Completeness limits and next action

This is complete for the pinned `symbiont/.../sensory/` and `modality/`
implementation/test trees, not an inventory of every Lab study or every
historical design document mentioning perception. Consumers cited above are
direct source import/test evidence or explicit cross-domain call sites; search
hits in prose are not runtime consumers. A separate Lab/Observation/Embodiment
inventory owns their remaining code and evidence. The host and vision modules
remain `DEFER` candidates, not accepted target code: determine their rightful
semantic owner and review their data/identity contracts before any migration.
No legacy code or compatibility layer is requested by this inventory.

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
limited to the pinned sensory package inventory; Modality's independent
versioning remains provisional under the owner decision above, not a permanent
topology claim, and this repository is not complete.
