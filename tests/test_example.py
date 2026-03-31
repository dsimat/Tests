import pytest

from test_package.example import distance, kinetic_energy


@pytest.mark.parametrize(
    "p1, p2, result",
    [
        ((3, 0), (0, 4), 5.0),
        ((1, 2), (4, 6), 5.0),
        ((0, 0), (0, 0), 0.0),
    ],
)
def test_distance(
    p1: tuple[float, float], p2: tuple[float, float], result: float
) -> None:
    """Test the distance function"""
    assert distance(p1, p2) == result
    assert distance(p2, p1) == result  # Symmetry test
    assert type(result) in (float, int)


@pytest.mark.parametrize(
    "mass, velocity, result",
    [(2, 3, 9), (0, 10, 0), (5, 0, 0), (1.5, 4, 12)],
)
def test_kinetic_energy(mass, velocity, result) -> None:
    """Test the kinetic_energy function"""
    assert kinetic_energy(mass, velocity) == result
    assert type(kinetic_energy(2, 3)) is float


# Failure example for testing purposes
# def test_distance_failure() -> None:
#     assert distance((1, 1), (4, 5)) == 6.0  # Incorrect expected value
