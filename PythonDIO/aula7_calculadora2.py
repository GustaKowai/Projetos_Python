class Calculadora:
    def __init__(self):
        pass
    def soma(self, a,b):
        return a + b
    def subtra(self, a,b):
        return a - b
    def multiplica(self, a,b):
        return a * b
    def divisao (self, a,b):
        return a / b

calculadora = Calculadora ()
#print(calculadora.a)
#print(calculadora.b)
print(calculadora.soma(10,2))
print(calculadora.subtra(5,3))
print(calculadora.multiplica(10,5))
print(calculadora.divisao(100,2))
# print(soma(10,2))
# print(subtra(10,2))
# print(multiplica(10,2))
# print(divisao(10,2))
