# Agent entrypoint — modality

**Status: migration-stage guidance.** This repository is a provisional independent repository and reserved capability seam. Its current package contains one explicitly ratified, fixture-specific stateless identity mapping for the first dimensionless scalar-field sensor, and no generic operator catalogue. Historical copy-first material is provenance, not current implementation or authorization. This is **not** a declaration of complete functionality or migration cut-over.

## Current ownership boundary

- **Current implementation:** `DimensionlessScalarFieldIdentityV1` validates and forwards only values in the ratified fixture range `[0, 1]`; it rejects invalid values rather than clipping. It assigns no environmental or cognitive meaning. Do not infer additional behavior from historical source material.
- **Repository role:** provisional independent boundary for future, explicitly specified transduction capabilities; this status does not make Modality a semantic authority or give it ownership of persistent domain state.
- **Does not own:** learned signal meaning, Organism state or objective Environment truth. Any future persistent modality-related state must be assigned to exactly one approved owner or declared implementation-ephemeral.
- Read [README.md](README.md) for current implemented scope and [MIGRATION.md](MIGRATION.md) for provenance, excluded work, source SHA, and deferred ownership. These local documents describe the extraction; they do not replace canonical constitutional or scientific authorities.

## Shared coordination guidance

- [Public organization governance](https://github.com/biopeia/.github/blob/main/GOVERNANCE.md)
- [Public contribution guidance](https://github.com/biopeia/.github/blob/main/CONTRIBUTING.md)
- [Private Repository Contract v1 — PROPOSED](https://github.com/biopeia/.github-private/blob/main/workflow/repository-contract-v1.md)
- [Private Biopeia Agent Workflow v1 — PROPOSED](https://github.com/biopeia/.github-private/blob/main/workflow/agent-workflow.md)
- [Biopeia coordination project](https://github.com/orgs/biopeia/projects/1)

These are links for human/agent reading, **not automatic instruction inheritance**. Verify that the tool in use has access to private resources and loads any required instructions explicitly.

## Execution constraints

1. Anchor all claims and work to a named base commit SHA; use a bounded Issue and PR with one accountable execution owner.
2. Classify work by established ORDINARY/SCIENTIFIC/FROZEN/CONSTITUTIONAL policy and evaluate risk separately. Do not infer approval from a label.
3. Identify cross-domain contracts and record consumers/producers, data ownership, version and compatibility; do not import another domain's private internals as a shortcut.
4. Technical CI validates implementation only. It does not prove scientific efficacy or authorize experiments, constitutional changes or promotion.
5. Preserve migration provenance and the original source; do not delete, transfer authority, start Pass 15, or claim cut-over without express authorization.
6. On conflicts between canonical sources, stop and request a documented decision. This file does not supersede protected instructions or approved ADRs.

This entrypoint introduces no new required CI gate, automatic merge, or package dependencies.
