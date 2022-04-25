class Calculadora:
    def __init__(self,num1,num2):
        self.a = num1
        self.b = num2
    def soma(self):
        return self.a + self.b
    def subtra(self):
        return self.a - self.b
    def multiplica(self):
        return self.a * self.b
    def divisao (self):
        return self.a / self.b
if __name__ == '__main__':

    calculadora = Calculadora (10,2)
    print(calculadora.a)
    print(calculadora.b)
    print(calculadora.soma())
    print(calculadora.subtra())
    print(calculadora.multiplica())
    print(calculadora.divisao())
    # print(soma(10,2))
    # print(subtra(10,2))
    # print(multiplica(10,2))
    # print(divisao(10,2))
