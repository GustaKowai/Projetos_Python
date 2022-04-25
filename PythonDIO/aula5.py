lista = [12,10,7,3,5]
lista_animal = ['cachorro', 'gato', 'elefante','lobo','arara']

tupla = (1,10,12,14)
print(tupla[3])
print(len(tupla))
print(len(lista_animal))
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)
lista_numerica = list(tupla)
print(type(lista_numerica))
print(lista_numerica)
#-- Organizações --
# lista.sort()
# lista_animal.sort()
# print(lista)
# print(lista_animal)
# lista_animal.reverse()
# print(lista_animal)

# soma = 0
# for x in lista:
#     soma += x
#     print(x)
# print(soma)
# print(sum(lista))
# print(max(lista))
# print(min(lista))
#
# print(min(lista_animal))
# # Ele busca pela palabra com "menor valor" alfabeticamente. Da para usar o max para isso também.
#
# nova_lista = lista_animal*3
# print(nova_lista)
# -- adiciona animais na sua lista --
# x = 'y'
# while x == 'y':
#     animal = input('Digite um animal para adicionar na lista: ')
#     if animal in lista_animal:
#         print('existe um {} na lista'.format(animal))
#     else:
#         print('não existe um {} na lista, será incluido.'.format(animal))
#         lista_animal.append(animal)
#     print(lista_animal)
#     x = input('deseja incluir mais um animal na lista? (y/n)')
# -- remove animais da lista--
# lista_animal.pop()
# print(lista_animal)
# lista_animal.remove('elefante')
# print(lista_animal)