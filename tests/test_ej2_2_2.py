import pytest
from src.ej2_2_2 import cumplidos

def test_cumplidos():
    assert cumplidos(3) == "1, 2, 3 años. "
    assert cumplidos(5) == "1, 2, 3, 4, 5 años. "
    assert cumplidos(7) == "1, 2, 3, 4, 5, 6, 7 años. "
    
    

@pytest.mark.parametrize(
    "input1, expected",
    [
        (3, "1, 2, 3 años. "),
        (5, "1, 2, 3, 4, 5 años. "),
        (7, "1, 2, 3, 4, 5, 6, 7 años. ")
    ]
)
def test_cumplidos(input1, expected):
    assert cumplidos(input1) == expected