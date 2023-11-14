import pytest
from src.ej2_2_5 import inversion


def test_inversion():
    assert inversion(13, 678, 6) == ""
    assert inversion(7, 1000, 2) == ""
    assert inversion(5, 789876, 10) == ""
    
    
@pytest.mark.parametrize(
    "input1, input2 , input3, expected",
    [
        (13, 678, 6, ""),
        (7, 1000, 2,""),
        (5, 789876, 10, "")
    ]
)
def test_inversion(input1, input2 , input3, expected):
    assert inversion(input1, input2 , input3) == expected