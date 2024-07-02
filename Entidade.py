from Ponto import *

class Entidade:
    Posicao:Ponto

    def __init__(self,posicao,angulo):
        self.Posicao = posicao
        self.Angulo = angulo

    def MovimentaEntidade(self):
    
        if(self.Angulo == 0):
            self.Posicao = self.Posicao.__add__(Ponto(0,0,0.4))
        