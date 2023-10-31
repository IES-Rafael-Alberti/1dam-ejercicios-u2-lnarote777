import pytest
from src.ej2_06 import grupo

def test_grupo():
    assert grupo("antonia", "f") == "Perteneces al grupo A"
    assert grupo("antonio", "m") == "Perteneces al grupo B"
    assert grupo("lucía", "f") == "Perteneces al grupo A"
    
    

@pytest.mark.parametrize(
    "input1, input2, expected",
    [
        ("antonia", "f", "Perteneces al grupo A"),
        ("antonio", "m", "Perteneces al grupo B"),
        ("lucía", "f", "Perteneces al grupo A")
    ]
)
def test_grupo(input1, input2, expected):
    assert grupo(input1 , input2) == expected