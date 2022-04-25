n = int(input('Entre o numero de regiões: '))
teste = int(input('Entre 0 se estiver correto'))
regioes = []
ordem = []
posit = 1
cont = 0
m = 1
justo = 0
for i in range(1, n + 1):
    regioes.append(i)
print(regioes)


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
            #print(ordem)
    #    print(posit)
    if ordem[n-1] == 13:
        justo = 1
        print('O valor justo é {}'.format(m))
        print(ordem)
    else:
        print(m)
        m += 1
        print(ordem)
