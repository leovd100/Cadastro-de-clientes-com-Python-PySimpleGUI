from datetime import datetime


def set_Name(nome):
    verify = any(char.isdigit() for char in nome) or (len(nome) <= 3)

    if verify == True:
        print('Nome inválido.Digite novamente, o nome deve conter apenas letras e deve ter no mínimo 8 caracteres')
    else:
        print('Nome válido')
        return True


def set_Age():

    try:
        age = int(input('Digite sua idade').strip())
        if len(str(age)) > 2:

            while len(str(age)) > 2:
                print('Idade inválida.Digite novamente')
                age = int(input('Digite sua idade').strip())
        return age
    except:
        print('Idade inválida.Digite novamente')


def set_Tell_fixo(phone):

    try:
        phone = int(phone)
        ddd = (str(phone)[:2])
        number = (str(phone))
        if 8 != len(str(phone)) and len(str(phone)) != 10:
            print('Telefone Inválido.Digite Novamente')
        elif len(str(phone)) == 10:
            print(f'Número : {ddd}{number[2:]}')
        else:
            print(f'Número :({number})')

    except:

        print('Telefone Inválido.Digite Novamente')

def set_email(email):
    email = email.strip()

    indexSign = email.find('@')
    if indexSign > 0:
        field = email[indexSign:]
        if ('.com' in field) or ('.br' in field):
            print('E-mail valido')
            return True
        else:
            print('E-mail inválido')
    else:
        print('E-mail inválido')


def get_hour():
    while True:
        h = datetime.now().hour
        m = datetime.now().minute
        s = datetime.now().second
        return f'{h}:{m}:{s}'

def desagrupar_numero_cpf(cpf):
    cpf = str(cpf).split('.')
    dig = cpf[2].split('-')
    cpf.remove(cpf[2])
    valor = ''
    for x in dig:
        cpf.append(x)
    for x in cpf:
       valor += x
    return int(valor)

def faze_conta_cpf(nwNumber, vlr):
    result_multi = 0
    result_rest = 0
    for value, num in enumerate(nwNumber):
        result_multi += ((value * -1) + vlr) * int(num)

    result_rest = (result_multi * 10) % 11
    if result_rest == 10:
        result_rest = 0
    return result_rest

def valida_cpf(numberCpf):
    if '.' in str(numberCpf):
        number = desagrupar_numero_cpf(numberCpf)
    else:
        number = str(numberCpf)

    dig = int(str(number)[-2:])
    nw_Number = str(number)[:9]

    nw_Number += str(faze_conta_cpf(nw_Number, 10))
    nw_Number += str(faze_conta_cpf(nw_Number, 11))

    if int(nw_Number) == int(number):
        print('CPF válido')
    else:

        print('CPF inválido')


