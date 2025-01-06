import numpy as np

class Pilha:
    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__topo = -1
        self.__valores = np.empty(capacidade, dtype=int)

    def __pilha_cheia(self):
        if(self.__topo == self.__capacidade -1):
            return True
        else:
            return False
        
    def __pilha_vazia(self):
        if(self.__topo == -1):
            return True
        else:
            return False
        
    def empilhar(self, valor):
        if(self.__pilha_cheia()):
            print('A pilha está cheia')
        else:
            self.__topo = self.__topo + 1
            self.__valores[self.__topo] = valor

    def desempilhar(self):
        if(self.__pilha_vazia()):
            print('A pilha está vazia')
        else:
            self.__topo = self.__topo -1

    def ver_topo(self):
        if(self.__pilha_vazia()):
            return -1
        else:
            return self.__valores[self.__topo]

pilha = Pilha(5)
print(pilha.ver_topo())
pilha.empilhar(1)
pilha.empilhar(2)
pilha.empilhar(3)
pilha.empilhar(4)
pilha.empilhar(5)
pilha.empilhar(6)
print(pilha.ver_topo())
pilha.desempilhar()
pilha.desempilhar()
pilha.desempilhar()
pilha.desempilhar()
print(pilha.ver_topo())
pilha.desempilhar()
pilha.desempilhar()
