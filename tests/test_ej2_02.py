import pytest
from src.ej2_02 import comprobarPassword


def test_comprobarPassword():
    assert comprobarPassword("contraseña") == "Tu contraseña coincide con la mía."
    assert comprobarPassword("ConTRAseña") == "Tu contraseña coincide con la mía."
    assert comprobarPassword("pedroPo") == "No coincide."
    
    
@pytest.mark.parametrize(
    "input_n, expected",
    [
        ("contraseña", "Tu contraseña coincide con la mía."),
        ("ConTRAseña", "Tu contraseña coincide con la mía."),
        ("pedroPo", "No coincide.")
    ]
)
def test_comprobarPassword(input_n, expected):
    assert comprobarPassword(input_n) == expected