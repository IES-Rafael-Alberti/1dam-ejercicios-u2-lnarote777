import pytest
from src.ej2_1_6 import grupo

def test_grupo():
    assert grupo("antonia", "f") == "A"
    assert grupo("antonio", "m") == "B"
    assert grupo("luca", "f") == "A"
    
    

@pytest.mark.parametrize(
    "input1, input2, expected",
    [
        ("antonia", "f", "A"),
        ("antonio", "m", "B"),
        ("luca", "f", "A")
    ]
)
def test_grupo(input1, input2, expected):
    assert grupo(input1 , input2) == expected