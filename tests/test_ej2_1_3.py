import pytest
from src.ej2_1_3 import division


def test_division():
    assert division(10 , 2) == 5
    assert division(8 , 4) == 2
    assert division(3 , 0) == "***ERROR*** - El divisor no puede ser 0."
    assert division(9 , 0) == "***ERROR*** - El divisor no puede ser 0."
    
    
    
@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
        (10 , 2, 5),
        (3 , 0 , "***ERROR*** - El divisor no puede ser 0."),
        (8, 4, 2),
        (9, 0 , "***ERROR*** - El divisor no puede ser 0.")
    ]
)
def test_division(input_n1, input_n2, expected):
    assert division(input_n1 , input_n2) == expected