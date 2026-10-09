import modality


def test_package_exposes_no_unratified_concrete_operator_or_catalogue():
    assert modality.__all__ == ()
