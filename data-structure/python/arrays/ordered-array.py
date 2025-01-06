import numpy as np

class VetorOrdenado:
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
            print('Capacidade máxima atingida')
            return
         
        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1
            
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1

        self.valores[posicao] = valor
        self.ultima_posicao += 1

    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] > valor:
                return -1
            if self.valores[i] == valor:
                return i
            if i == self.ultima_posicao:
                return -1
            
    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]

            self.ultima_posicao -= 1

vetor = VetorOrdenado(10)
vetor.imprime()
vetor.insere(6)
vetor.insere(4)
vetor.insere(3)
vetor.insere(8)
vetor.insere(5)
print(vetor.pesquisar(5))
print(vetor.pesquisar(2))
print(vetor.pesquisar(9))
vetor.excluir(5)
vetor.excluir(8)
vetor.excluir(3)
print(vetor.excluir(9))
vetor.imprime()

    

""" 
Minha solução

import numpy as np

class VetorOrdenado:
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
    
    def pesquisa(self, valor):        
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] >= valor:
                return i
        return -1      
    
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade -1:
            print('O vetor está cheio')
            return 
        
        indice = self.pesquisa(valor)
        
        self.ultima_posicao += 1    
        if indice == -1:
            self.valores[self.ultima_posicao] = valor
            return self.ultima_posicao
        

        for i in range(self.ultima_posicao, indice, -1):
            self.valores[i] = self.valores[i - 1]
        
        self.valores[indice] = valor
        return self.ultima_posicao




                

vetorOrdenado = VetorOrdenado(10)
vetorOrdenado.imprime()
vetorOrdenado.insere(2)
vetorOrdenado.insere(5)
vetorOrdenado.insere(3)
vetorOrdenado.insere(8)
vetorOrdenado.insere(7)
vetorOrdenado.insere(10)
vetorOrdenado.insere(1)
vetorOrdenado.insere(6)
vetorOrdenado.insere(4)
vetorOrdenado.insere(0)
vetorOrdenado.imprime()
vetorOrdenado.insere(12)
vetorOrdenado.insere(15)
print(vetorOrdenado.pesquisa(3)) """