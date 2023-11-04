import pytest
from src.ej2_2_9 import comprobarPassword

def test_comprobarPassword():
    assert comprobarPassword("contraseña") == "Contraseña correcta."
    assert comprobarPassword("ConTRAseña") == "Contraseña correcta."
    
    
@pytest.mark.parametrize(
    "input_n, expected",
    [
        ("contraseña", "Contraseña correcta."),
        ("ConTRAseña", "Contraseña correcta.")
    ]
)
def test_comprobarPassword(input_n, expected):
    assert comprobarPassword(input_n) == expected