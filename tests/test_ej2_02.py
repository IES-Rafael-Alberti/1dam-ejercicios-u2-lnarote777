import pytest
from src.ej2_02 import comporbarPassword


def test_comprobarPassword():
    assert comporbarPassword("contraseña") == True
    assert comporbarPassword("ConTRAseña") == True
    assert comporbarPassword("pedroPo") == False
    
    
@pytest.mark.parametrize(
    "input_n, expected",
    [
        ("contraseña", True),
        ("ConTRaseña", True),
        ("pedroPo", False),
    ]
)
def comporbarPassword(input_n,expected):
    assert mayorEdad(input_n) == expected