
lista = [1,10]
arquivo = open('teste.txt','r')
try:
    print('Abrir arquivo')
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]

    x = 2
except ZeroDivisionError:
    print('Não é possível realizar uma divisão por zero')
except IndexError:
    print('Erro ao acessar um indice invalido da lista')
except BaseException as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))
else:
    print('Executa quando não ocorre nenhuma exceção')
finally:
    print('Sempre executa')
    print('fechando arquivo')
    arquivo.close()