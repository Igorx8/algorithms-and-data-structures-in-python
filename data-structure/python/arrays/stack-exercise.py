import numpy as np

class Stack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__top = -1
        self.__values = np.empty(capacity, dtype=str)
        """ self.__values = np.chararray(self.__capacity, unicode=true) """

    
    def __filled(self):
        if(self.__top == self.__capacity -1):
            return True
        else:
            return False
        
    def __empty(self):
        if(self.__top == -1):
            return True
        else:
            return False
        
    def push(self, value):
        if(self.__filled()):
            print('The stack is already filled')
        else:
            self.__top += 1
            self.__values[self.__top] = value

    def pop(self):
        if(self.__empty()):
            print('The stack is empty')
        else:
            self.__top -= 1

    def top(self):
        if(self.__empty()):
           return -1
        else:
            return self.__values[self.__top]
        
    def validate(self, text):
        openers = ['{', '[', '(']
        closers = ['}', ']', ')']
        try:
            for i in range(len(text)):
                if(text[i] in openers):
                    self.push(text[i])
                if(text[i] in closers):
                    if(text[i] == '}'):
                        if(self.__values[self.__top] == '{'):
                            self.pop()
                            continue
                    if(text[i] == ']'):
                        if(self.__values[self.__top] == '['):
                            self.pop()
                            continue
                    if(text[i] == ')'):
                        if(self.__values[self.__top] == '('):
                            self.pop()
                            continue
                    raise ValueError(f"Valor de fechamento inválido na posição: {i}")
            if(self.__top != -1):
                raise ValueError(f"Tag sem fechamento: {self.__values[self.__top]}")
        except ValueError as e:
            return print(e)
        print('O texto inserido está correto')





    
text = input('Digite o texto para a validação: ')

stack = Stack(len(text))
stack.validate(text)