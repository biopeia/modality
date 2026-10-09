import pytest

from modality import DEFAULT_MODALITIES, SensoryModality, TransductionKind


def test_default_catalog_is_immutable_and_validated():
    assert len(DEFAULT_MODALITIES) == 4
    assert all(item.max_inputs > 0 for item in DEFAULT_MODALITIES)
    assert DEFAULT_MODALITIES[0].allowed_transductions == (TransductionKind.IDENTITY,)


@pytest.mark.parametrize(
    "kwargs",
    [
        {"modality_id": "has space"},
        {"allowed_transductions": ()},
        {"max_inputs": 0},
        {"temporal_capacity": 0},
        {"base_cost": 0.0},
    ],
)
def test_modality_descriptor_rejects_invalid_values(kwargs):
    values = {
        "modality_id": "valid",
        "allowed_transductions": (TransductionKind.IDENTITY,),
        "max_inputs": 1,
        "temporal_capacity": 1,
        "base_cost": 0.1,
    }
    values.update(kwargs)
    with pytest.raises(ValueError):
        SensoryModality(**values)
