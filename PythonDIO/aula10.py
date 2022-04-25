from datetime import date, time, datetime, timedelta

def trabalhando_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%A %d/%m/%Y')
    print(data_atual_str)

def trabalhando_time():
    horario = time(hour=15, minute=18, second=30)
    print(now.strftime('%H hours, %M minutes and %S seconds'))

def trabalhando_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y - %H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.weekday())
    tupla = ('Segunda','Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(1994, 4, 20, 15, 30, 20)
    print(data_criada.strftime('%c'))
    print(data_criada)
    data_string = '01/01/2019 15:12:34'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    nova_data = data_convertida - timedelta(days=365, minutes=-15)
    print(nova_data)

if __name__ == '__main__':
    #trabalhando_date()
    #trabalhando_time()
    trabalhando_datetime()