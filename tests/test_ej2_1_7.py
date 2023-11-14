import pytest
from src.ej2_1_7 import impositivo


def test_impositivo():
    assert impositivo(10000000) == "45%"
    assert impositivo(43672) == "30%"
    assert impositivo(3092) == "5%"
    assert impositivo(20080) == "20%"
    
    
    
@pytest.mark.parametrize(
    "input_n, expected",
    [
        (10000000,"45%"),
        (3092, "5%"),
        (43672, "30%"),
        (20080, "20%")
    ]
)
def test_impositivo(input_n, expected):
    assert impositivo(input_n) == expected
    