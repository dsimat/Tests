import math


def distance(
    p1: tuple[float | int, float | int], p2: tuple[float | int, float | int]
) -> float | int:
    """Compute the Euclidean distance between points p1 and p2 (2D coordinates)."""
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])


def kinetic_energy(mass: float | int, velocity: float | int) -> float | int:
    """Compute kinetic energy"""
    return 0.5 * mass * velocity**2
