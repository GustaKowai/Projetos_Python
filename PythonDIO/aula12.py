import requests

def retorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    print(response.status_code)
    dados_cep = response.json() #json é um dicionário
    print(response.json())
    print(dados_cep['logradouro'])
    print(dados_cep['bairro'])
    return dados_cep

def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

def retorna_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    response = retorna_response('https://web.dio.me/course/introducao-a-programacao-com-python/learning/b39d7534-d57b-40e5-ab7c-c664fefb0aa0')
    print(response)
    #retorna_dados_cep('13566810')
    #dados_pokemon = retorna_dados_pokemon('pikachu')
    #print(dados_pokemon['sprites']['front_shiny'])