import pytest
from src.ej2_2_4 import cuenta_atras



def test_cuenta_atras():
    assert cuenta_atras(13) == "13, 12, 11, 10, 9, 8, 7, 6 ,5 ,4 ,3, 2, 1, 0. "
    assert cuenta_atras(7) == "7, 6, 5, 4, 3, 2, 1, 0. "
    assert cuenta_atras(5) == "5, 4, 3, 2, 1, 0. "
    
    
@pytest.mark.parametrize(
    "input_n, expected",
    [
        (13, "13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0. "),
        (7, "7, 6, 5, 4, 3, 2, 1, 0. "),
        (5, "5, 4, 3, 2, 1, 0. ")
    ]
)
def test_cuenta_atras(input_n, expected):
    assert cuenta_atras(input_n) == expected