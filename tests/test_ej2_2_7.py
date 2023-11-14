import pytest
from src.ej2_2_7 import multiplicacion


def test_multiplicacion():
    assert multiplicacion("") == ""
    assert multiplicacion("") == ""
    assert multiplicacion("") == ""
    
    
@pytest.mark.parametrize(
    "input1, expected",
    [
        ("" ,""),
        ("",""),
        ("", "")
    ]
)
def test_multiplicacion(input1, expected):
    assert multiplicacion(input1) == expected