import pytest
from src.ej2_1_9 import cobro

def test_cobro():
    assert cobro(18) ==  "10€"
    assert cobro(11) ==  "5€"
    assert cobro(3) == "Gratis"
    
    

@pytest.mark.parametrize(
    "input1, expected",
    [
        (18, "10€"),
        (11,"5€"),
        (3, "Gratis")
    ]
)
def test_cobro(input1, expected):
    assert cobro(input1 )== expected