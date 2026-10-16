"""Unit tests for KinematicSomaticTransductionV1."""

from __future__ import annotations

from dataclasses import dataclass
import math
import pytest

from modality import (
    KinematicSomaticTransductionV1,
    KinematicTransductionError,
)


@dataclass(frozen=True, slots=True)
class DummyJoint:
    joint_id: str
    position_rad: float
    velocity_rad_per_s: float


def test_kinematic_somatic_transduction_valid() -> None:
    transduction = KinematicSomaticTransductionV1()
    joints = (
        DummyJoint("joint.hinge", 0.25, -1.5),
        DummyJoint("joint.wrist", 0.0, 0.5),
    )
    result = transduction.transduce(joints)
    assert result == {
        "joint.hinge:pos": 0.25,
        "joint.hinge:vel": -1.5,
        "joint.wrist:pos": 0.0,
        "joint.wrist:vel": 0.5,
    }
    assert transduction.CONTRACT_ID == "biopeia.modality.kinematic-somatic-transduction"
    assert transduction.REVISION == 1


def test_kinematic_somatic_transduction_empty() -> None:
    transduction = KinematicSomaticTransductionV1()
    assert transduction.transduce(()) == {}
    assert transduction.transduce([]) == {}


@pytest.mark.parametrize(
    "invalid_joints,match",
    [
        (None, "sequence"),
        ("not-a-sequence", "sequence"),
        (123, "sequence"),
        ({"joint.hinge": 0.1}, "sequence"),
    ],
)
def test_kinematic_somatic_transduction_rejects_non_sequence(invalid_joints, match) -> None:
    transduction = KinematicSomaticTransductionV1()
    with pytest.raises(KinematicTransductionError, match=match):
        transduction.transduce(invalid_joints)  # type: ignore


@pytest.mark.parametrize(
    "joint,match",
    [
        (DummyJoint("", 0.1, 0.2), "non-empty string"),
        (DummyJoint("   ", 0.1, 0.2), "non-empty string"),
        (DummyJoint(None, 0.1, 0.2), "non-empty string"),  # type: ignore
        (DummyJoint("j1", True, 0.2), "must be numeric"),  # boolean position
        (DummyJoint("j1", 0.1, False), "must be numeric"),  # boolean velocity
        (DummyJoint("j1", "0.1", 0.2), "must be numeric"),  # string position
        (DummyJoint("j1", 0.1, "0.2"), "must be numeric"),  # string velocity
        (DummyJoint("j1", float("nan"), 0.2), "must be finite"),
        (DummyJoint("j1", float("inf"), 0.2), "must be finite"),
        (DummyJoint("j1", 0.1, float("-inf")), "must be finite"),
    ],
)
def test_kinematic_somatic_transduction_negative_cases(joint, match) -> None:
    transduction = KinematicSomaticTransductionV1()
    with pytest.raises(KinematicTransductionError, match=match):
        transduction.transduce([joint])
