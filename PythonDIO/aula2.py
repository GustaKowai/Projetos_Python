a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
soma = a + b
subtra = a - b
multi = a * b
divi = a / b
resto = a % b
#print(type(soma))
#soma = str(soma)
#print(type(soma))
resultado = ('Soma = {som} \nSubtração = {sub} \nMultiplicação = {mul}'
'\nDivisão = {divi}'
'\nResto = {res}' .format(som=soma,sub=subtra, mul=multi, divi=divi, res=resto))
print(resultado)
#print('soma = ' + str(soma))
#print('subtração = ' + str(subtra))
#print(multi)
#print(divi)
#print(resto)
