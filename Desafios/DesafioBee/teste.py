x = 1
inicio = []
resultado = []
# Receber todas as entradas
while x != 0:
    x = int(input())
    if x != 0:
        inicio.append(x)

for n in inicio:
    regioes = []
    ordem = []
    posit = 1
    cont = 0
    m = 1
    justo = 0
    #print(n)
    for i in range(1, n + 1):
        regioes.append(i)
        #print(regioes)
        #print(justo)
    while justo == 0:
        ordem = []
        ordem.append(regioes[0])
        posit = 0
        cont = 0
        while len(ordem) < len(regioes):
            #print('O comprimento da ordem é {}'.format(len(ordem)))
            #print(posit)
            if regioes[posit] in ordem:
                posit += 1
                if posit > n-1:
                    posit = posit - n
            else:
                cont +=1
                posit += 1
                if posit > n-1:
                    posit = posit - n
            if cont == m:
                cont = 0
                ordem.append(regioes[posit-1])
        if ordem[n-1] == 13:
            justo = 1
            resultado.append(m)
        else:
            m += 1
for y in resultado:
    #print(resultado)
    print(y)