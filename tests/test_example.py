from test_package.example import distance, kinetic_energy
import math


def test_distance() -> None:
    assert distance((3, 0), (0, 4)) == 5.0
    assert distance((1, 2), (4, 6)) == 5.0
    assert distance((0, 0), (0, 0)) == 0.0
    assert distance((-1, -1), (1, 1)) == math.hypot(2, 2)
    assert type(distance((1, 2), (4, 6))) is float


def test_kinetic_energy() -> None:
    assert kinetic_energy(2, 3) == 9.0
    assert kinetic_energy(0, 10) == 0.0
    assert kinetic_energy(5, 0) == 0.0
    assert kinetic_energy(1.5, 4) == 12.0
    assert type(kinetic_energy(2, 3)) is float


# Failure example for testing purposes
# def test_distance_failure() -> None:
#     assert distance((1, 1), (4, 5)) == 6.0  # Incorrect expected value
