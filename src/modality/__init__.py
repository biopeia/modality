"""Reusable, non-authoritative modality and transduction contracts."""

from .modalities import DEFAULT_MODALITIES, SensoryModality
from .transduction import TransductionKind, apply_transduction

__all__ = [
    "DEFAULT_MODALITIES",
    "SensoryModality",
    "TransductionKind",
    "apply_transduction",
]
