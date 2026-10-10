import math

import pytest

from modality import (
    DimensionlessScalarFieldIdentityV1,
    ScalarFieldTransductionError,
)


def test_first_scalar_field_transduction_is_explicit_identity():
    mapping = DimensionlessScalarFieldIdentityV1()

    assert mapping.CONTRACT_ID == "biopeia.modality.dimensionless-scalar-field-identity"
    assert mapping.REVISION == 1
    assert mapping.QUANTITY_KIND == "dimensionless_scalar_field"
    assert mapping.UNIT == "1"
    assert (mapping.MINIMUM, mapping.MAXIMUM) == (0.0, 1.0)
    assert mapping.transduce(0.0) == 0.0
    assert mapping.transduce(0) == 0.0
    assert mapping.transduce(0.375) == 0.375
    assert mapping.transduce(1.0) == 1.0
    assert mapping.transduce(1) == 1.0


@pytest.mark.parametrize(
    "value",
    [-0.01, 1.01, math.nan, math.inf, -math.inf, 10**400, True, "0.5"],
)
def test_first_scalar_field_transduction_rejects_invalid_values(value):
    with pytest.raises(ScalarFieldTransductionError):
        DimensionlessScalarFieldIdentityV1().transduce(value)
