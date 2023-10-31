
from src.ej2_06 import grupo

def test_grupo():
    assert grupo(antonia, mujer) == "Perteneces al grupo: A"
    assert grupo(nacho, hombre) == "Perteneces al grupo: A"
    assert grupo(jose, hombre) == "Perteneces al grupo: B"
    assert grupo(antonio, hombre) == "Perteneces al grupo: B"