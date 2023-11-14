import pytest
from src.ej2_2_6 import triangulo


def test_triangulo():
    assert triangulo(13) == ""
    assert triangulo(7) == ""
    assert triangulo(5) == ""
    
    
@pytest.mark.parametrize(
    "input1, expected",
    [
        (13 ,""),
        (7,""),
        (5, "")
    ]
)
def test_triangulo(input1, expected):
    assert triangulo(input1) == expected