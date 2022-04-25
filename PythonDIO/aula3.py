# O melhor seria um "while" pois a pessoa poderia errar mais de uma vez e com o while +
# + da para corrigir enquanto estiver errado.

a = int(input('Primeiro Bimestre: '))
if a > 10 or a < 0:
    a = int(input('Você digitou errado. \n Primeiro Bimestre: '))
b = int(input('Segundo Bimestre: '))
if b > 10 or b < 0:
    b = int(input('Você digitou errado. \n Segundo Bimestre: '))
c = int(input('terceiro Bimestre: '))
if c > 10 or c < 0:
    c = int(input('Você digitou errado. \n Terceiro Bimestre: '))
d = int(input('Quarto Bimestre: '))
if d > 10 or d < 0:
    d = int(input('Você digitou errado. \n Quarto Bimestre: '))
media = (a+b+c+d)/4
print('média: {}'.format(media))


# Checagem após todas as notas serem informadas
# if a <= 10 and b <=10 and c <= 10 and d <= 10:
#     print('média: {}'.format(média)')
# else
#     print('Alguma nota foi informada incorretamente.')

# ------ checagem se tem algum número par --------
# a = int(input('Entre com o primeiro valor: '))
# b = int(input('Entre com o segundo valor: '))
# resto_a = a % 2
# resto_b = b % 2
# if resto_a == 0 or not resto_b > 0:
#     print('Foi digitado pelo menos um número par')
# else:
#     print('Nenhum número par foi digitado')
# ------- Checagem se o número é par ou ímpar-----
# if resto == 0:
#    print('O número é par')
# else:
#    print('O número é ímpar')

# ---- Busca pelo maior número------
# a = int(input('Por favor, informe o primeiro valor: '))
# b = int(input('Por favor, informe o segundo valor: '))
# c = int(input('Por favor, informe o terceiro valor: '))
# if a > b and b > c:
#     print('O maior número é {}'.format(a))
# elif b > c: # Não precisa checar o b > a!
#     print('O maior número é {}' .format(b))
# else:
#     print('O maior número é {}'.format(c))
# print('Final do programa')
