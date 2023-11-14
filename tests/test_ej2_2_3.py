import pytest
from src.ej2_2_3 import impar

def test_impar():
    assert impar(13) == "1, 3, 5, 7, 9, 11, 13. "
    assert impar(7) == "1, 3, 5, 7. "
    assert impar(5) == "1, 3, 5. "
    
    
@pytest.mark.parametrize(
    "input_n, expected",
    [
        (13, "1, 3, 5, 7, 9, 11, 13. "),
        (7, "1, 3, 5, 7. "),
        (5, "1, 3, 5. ")
    ]
)
def test_impar(input_n, expected):
    assert impar(input_n) == expected