from Ponto import *
from enum import Enum

class Camera:
    
    Posicao = Ponto(0,0,0)
    Foco = Ponto(0,0,0)
    TipoDeCamera = None
    
    def __init__(self,ponto,foco,numeroTipo):
        Posicao = ponto
        Foco = foco
        TipoDeCamera = Tipo.numeroTipo


class Tipo(Enum):
    PrimeiraPessoa = 1
    TerceiraFocoMapa = 2
    TerceiraFocoPlayer = 3