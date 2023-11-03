import pytest
from src.ej2_1_4 import par


def test_par():
    assert par(2)== "2 es par."
    assert par(7)== "7 es impar."
    assert par(483) == "483 es impar."
    assert par(14) == "14 es par."
    

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (2, "2 es par."),
        (7, "7 es impar."),
        (483,"483 es impar."),
        (14, "14 es par.")
    ]
)
def test_par(input_n, expected):
    assert par(input_n) == expected