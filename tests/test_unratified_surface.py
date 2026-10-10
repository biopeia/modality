import modality


def test_package_exposes_only_the_ratified_fixture_specific_mapping():
    assert set(modality.__all__) == {
        "DimensionlessScalarFieldIdentityV1",
        "ScalarFieldTransductionError",
    }
    assert not hasattr(modality, "apply_transduction")
    assert not hasattr(modality, "TransductionKind")
    assert not hasattr(modality, "SensoryModality")
