import numpy as np

class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(f"{i} -- {self.valores[i]}")

    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('O vetor está cheio')
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor

    def pesquisa(self, valor):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] == valor:
                return i
        return -1
    
    def remove(self, valor):
        indice = self.pesquisa(valor)
        if indice == -1:
            return indice
        else:
            for i in range(indice, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            self.ultima_posicao -= 1

vetor = VetorNaoOrdenado(5)
vetor.insere(3)
vetor.insere(5)
vetor.insere(8)
vetor.insere(1)
vetor.insere(7)
vetor.imprime()

vetor.remove(8)
print(vetor.remove(15))
vetor.imprime()
vetor.insere(2)
vetor.imprime()