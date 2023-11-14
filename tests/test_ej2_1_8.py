import pytest
from src.ej2_1_8 import puntuacion


def test_puntuacion():
    assert puntuacion(0.6) == None
    assert puntuacion(0.9) == None
    assert puntuacion(0.4) == None
    
    
@pytest.mark.parametrize(
    "input_n, expected",
    [
        (0.6, None ),
        (0.9, None),
        (0.4, None )
    ]
)
def test_puntuacion(input_n, expected):
    assert puntuacion(input_n) == expected