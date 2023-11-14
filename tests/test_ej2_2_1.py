import pytest
from src.ej2_2_1 import rep


def test_rep():
    assert rep("luca") == "luca"
    assert rep("hola") == "hola"
    assert rep("PedroPicaPiedra") == "PedroPicaPiedra"
    
    
@pytest.mark.parametrize(
    "input_n, expected",
    [
        ("luca", "luca" ),
        ("hola", "hola"),
        ("PedroPicaPiedra", "PedroPicaPiedra")
    ]
)
def test_rep(input_n, expected):
    assert rep(input_n) == expected