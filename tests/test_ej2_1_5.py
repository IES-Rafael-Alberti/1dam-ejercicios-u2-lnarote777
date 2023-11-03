import pytest
from src.ej2_1_5 import tributar


def test_tributar():
    assert tributar(17, 2864) == "Usted puede tributar."
    assert tributar(64, 987) =="Usted no puede tributar."
    assert tributar(15, 30865) == "Usted no puede tributar."
    assert tributar(16, 1000) == "Usted puede tributar."
    
    
    
@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
        (64, 987, "Usted no puede tributar."),
        (15, 30865, "Usted no puede tributar."),
        (17, 2864, "Usted puede tributar."),
        (26, 1000, "Usted puede tributar.")
    ]
)
def test_tributar(input_n1, input_n2, expected):
    assert tributar(input_n1, input_n2) == expected