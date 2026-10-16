"""Fixture-specific kinematic interoceptive transduction for revolute joints.

Transduces verified joint kinematics into opaque somatic observations conforming
to ADR-0094 and ADR-0099. Does not assign environmental meaning or anatomical authority.
"""

from __future__ import annotations

import math
from typing import ClassVar, Mapping, Protocol, runtime_checkable


class KinematicTransductionError(ValueError):
    """Input does not satisfy the kinematic transduction contract."""


@runtime_checkable
class JointKinematicInput(Protocol):
    """Structural protocol matching Embodiment's JointKinematicState."""

    joint_id: str
    position_rad: float
    velocity_rad_per_s: float


class KinematicSomaticTransductionV1:
    """Interoceptive transduction contract for revolute joint kinematics.

    Converts verified revolute joint physical states (position in radians,
    velocity in rad/s) into finite, bounded numeric observations for Organism.
    Assigns no anatomical semantics; keys are opaque channel descriptors.
    """

    CONTRACT_ID: ClassVar[str] = "biopeia.modality.kinematic-somatic-transduction"
    REVISION: ClassVar[int] = 1
    POSITION_UNIT: ClassVar[str] = "rad"
    VELOCITY_UNIT: ClassVar[str] = "rad/s"

    def transduce(
        self,
        joints: tuple[JointKinematicInput, ...] | list[JointKinematicInput],
    ) -> dict[str, float]:
        """Transduce joint states into a validated somatic observation mapping.

        Rejects non-finite values, non-string IDs, booleans, and malformed entries.
        """
        if not isinstance(joints, (tuple, list)):
            raise KinematicTransductionError("joints must be a sequence of joint kinematic states")

        result: dict[str, float] = {}
        for item in joints:
            joint_id = getattr(item, "joint_id", None)
            if not isinstance(joint_id, str) or not joint_id.strip():
                raise KinematicTransductionError("joint_id must be a non-empty string")

            pos = getattr(item, "position_rad", None)
            if isinstance(pos, bool) or not isinstance(pos, (int, float)):
                raise KinematicTransductionError(f"position_rad for {joint_id} must be numeric")
            if not math.isfinite(pos):
                raise KinematicTransductionError(f"position_rad for {joint_id} must be finite")

            vel = getattr(item, "velocity_rad_per_s", None)
            if isinstance(vel, bool) or not isinstance(vel, (int, float)):
                raise KinematicTransductionError(f"velocity_rad_per_s for {joint_id} must be numeric")
            if not math.isfinite(vel):
                raise KinematicTransductionError(f"velocity_rad_per_s for {joint_id} must be finite")

            result[f"{joint_id}:pos"] = float(pos)
            result[f"{joint_id}:vel"] = float(vel)

        return result


__all__ = [
    "JointKinematicInput",
    "KinematicSomaticTransductionV1",
    "KinematicTransductionError",
]
