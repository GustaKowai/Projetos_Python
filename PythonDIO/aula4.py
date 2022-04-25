a = int(input('Primeiro Bimestre: '))
while a > 10 or a < 0:
    a = int(input('Você digitou errado. \n Primeiro Bimestre: '))
b = int(input('Segundo Bimestre: '))
while b > 10 or b < 0:
    b = int(input('Você digitou errado. \n Segundo Bimestre: '))
c = int(input('terceiro Bimestre: '))
while c > 10 or c < 0:
    c = int(input('Você digitou errado. \n Terceiro Bimestre: '))
d = int(input('Quarto Bimestre: '))
while d > 10 or d < 0:
    d = int(input('Você digitou errado. \n Quarto Bimestre: '))
media = (a+b+c+d)/4
print('média: {}'.format(media))
# -- Funcionamento do while --

# a = 0
# while a < 10:
#     print(a)
#     a += 1


# ---- Detecta todos os numeros primos menores do que o numero digitado ----
# a = int(input('Digite um número: '))
#
# for num in range (a+1):
#     div = 0
#     for x in range (1, num+1):
#         resto = num % x
#         if resto == 0:
#             div += 1
#     if div == 2:
#         print('O Número {} é primo'.format(num))

# ---- Detecta se o numero é primo ----
# a = int(input('Digite um número: '))
# div = 0
# for x in range (1, a + 1):
#     resto = a % x
#     if resto == 0:
#         div += 1
# if div == 2:
#     print('O Número {} é primo'.format(a))
# else:
#     print('O número {} não é primo'.format(a))

# for x in range(1,101):
#     print(x)