import math

import pytest

from modality import TransductionKind, apply_transduction


@pytest.mark.parametrize(
    ("kind", "values", "previous", "integrator", "expected", "next_previous", "next_integrator"),
    [
        (TransductionKind.IDENTITY, [2.0], None, 0.0, 2.0, 2.0, 0.0),
        (TransductionKind.DIFFERENCE, [3.0], 1.0, 0.0, 2.0, 3.0, 0.0),
        (TransductionKind.DIFFERENCE, [3.0], None, 0.0, 0.0, 3.0, 0.0),
        (TransductionKind.INTEGRATE, [4.0], None, 2.0, 2.4, 4.0, 2.4),
        (TransductionKind.THRESHOLD, [2.0], None, 0.0, 1.0, 2.0, 0.0),
        (TransductionKind.MIX, [2.0, 4.0], None, 0.0, 3.0, 2.0, 0.0),
    ],
)
def test_transduction_primitives(kind, values, previous, integrator, expected, next_previous, next_integrator):
    output, actual_previous, actual_integrator = apply_transduction(
        kind,
        values,
        gain=1.0,
        decay=0.8,
        threshold=1.0,
        previous=previous,
        integrator=integrator,
    )
    assert output == pytest.approx(expected)
    assert actual_previous == next_previous
    assert actual_integrator == pytest.approx(next_integrator)


@pytest.mark.parametrize(
    "kwargs",
    [
        {"values": []},
        {"values": [math.inf]},
        {"values": [1.0], "gain": 0.0},
        {"values": [1.0], "decay": 1.1},
        {"values": [1.0], "threshold": math.nan},
    ],
)
def test_transduction_rejects_invalid_inputs(kwargs):
    args = {
        "kind": TransductionKind.IDENTITY,
        "values": [1.0],
        "gain": 1.0,
        "decay": 0.5,
        "threshold": 0.0,
        "previous": None,
        "integrator": 0.0,
    }
    args.update(kwargs)
    with pytest.raises(ValueError):
        apply_transduction(**args)


def test_transduction_output_is_bounded():
    output, _, _ = apply_transduction(
        TransductionKind.MIX,
        [1_000_000.0, 1_000_000.0],
        gain=8.0,
        decay=0.0,
        threshold=0.0,
        previous=None,
        integrator=0.0,
    )
    assert output == 1_000_000.0
