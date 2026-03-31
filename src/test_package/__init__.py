from test_package.example import distance, kinetic_energy
from test_package.factorial import factorial

# Expose the functions in the package's namespace
# This allows users to import them directly from the package, e.g.:
# from test_package import distance, kinetic_energy, factorial
__all__ = ["distance", "kinetic_energy", "factorial"]
