"""Fixture-specific numeric transduction for the first scalar-field sensor.

This module defines no environmental phenomenon or sensory meaning. It only
validates and forwards the finite, dimensionless scalar used by the ratified
first-sensor fixture. Identity here is explicit and revisioned; it is not a
generic operator catalogue or a persistent Modality-owned state.
"""

from __future__ import annotations

import math
from typing import ClassVar


class ScalarFieldTransductionError(ValueError):
    """Input does not satisfy the first scalar-field transduction contract."""


class DimensionlessScalarFieldIdentityV1:
    """Stateless identity mapping for the bounded first-sensor fixture.

    The source and result are dimensionless scalars in ``[0, 1]``. The
    surrounding Environment, Embodiment, World, and Organism contracts retain
    their own identities and provenance; this mapping transports none of
    those identities and assigns no semantic interpretation to the value.
    """

    CONTRACT_ID: ClassVar[str] = (
        "biopeia.modality.dimensionless-scalar-field-identity"
    )
    REVISION: ClassVar[int] = 1
    QUANTITY_KIND: ClassVar[str] = "dimensionless_scalar_field"
    UNIT: ClassVar[str] = "1"
    MINIMUM: ClassVar[float] = 0.0
    MAXIMUM: ClassVar[float] = 1.0

    def transduce(self, value: float) -> float:
        """Return an in-range finite value unchanged; never clip or coerce."""

        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ScalarFieldTransductionError("value must be numeric, not boolean")
        try:
            finite = math.isfinite(value)
        except OverflowError:
            finite = False
        if not finite:
            raise ScalarFieldTransductionError("value must be finite")
        if not self.MINIMUM <= value <= self.MAXIMUM:
            raise ScalarFieldTransductionError("value is outside the declared [0, 1] range")
        return float(value)


__all__ = ["DimensionlessScalarFieldIdentityV1", "ScalarFieldTransductionError"]
