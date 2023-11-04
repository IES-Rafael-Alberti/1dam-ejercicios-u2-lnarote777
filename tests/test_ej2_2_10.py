import pytest
from src.ej2_2_10 import es_primo


def test_es_primo():
    assert es_primo(98)== "No es primo"
    assert es_primo(7)== "Es primo"
    assert es_primo(483) == "Es primo"
    assert es_primo(14) == "No es primo"
    

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (98, "No es primo"),
        (7, "Es primo"),
        (483,"Es primo"),
        (14, "No es primo")
    ]
)
def test_es_primo(input_n, expected):
    assert es_primo(input_n) == expected