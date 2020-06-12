import PySimpleGUI as sg
from Cadastro import set_email,set_Name, valida_cpf,set_Tell_fixo
from BuscaCep import consultacep

class Tela_Cadastro:
    def __init__(self):
        layout = [

            [sg.Text(' Nome'),sg.Input(size=(25,1),key='name',)
                ,sg.Text('Idade '),sg.Input(size=(5,1),key='age')],

            [sg.Text('CPF   '),sg.Input(size=(15,2),key='cpf'),
             sg.Text('Telefone   '),sg.Input(size=(11,3),key='tel')],

             [sg.Text('E-mail'),sg.Input(size=(38,3),key='email')],

            [sg.Text('CEP  '),sg.Input(size=(10,4),key='cep'),
             sg.Text('Bairro'),sg.Input(size=(20,4),key='bairro')],
            [sg.Text('Rua   '),sg.Input(size=(25,5),key='rua'),
             sg.Text('Nº'),sg.Input(size=(5,5),key='number')],


            [sg.Button('Salvar'),sg.Button('Buscar CEP')],
            [sg.Output(size=(50, 5))]



        ]

        self.tela = sg.Window('Cadastro de Cliente',layout)



        flag_email = False
        flag_Name = False

        list_Triggers = {

                'tr_name':False,
                'tr_cpf':False,

                'tr_phone':False,
                'tr_cep':False,
                'tr_email':False,


        }




        while True:
            evento, self.values = self.tela.Read()

            #busca o CEP e faz um tratamento de erro caso não ache
            if evento == 'Buscar CEP':
                try:
                    consulta = consultacep(self.values['cep'])
                    self.tela.Element('rua').update(consulta['logradouro'])
                    self.tela.Element('bairro').update(consulta['bairro'])
                    list_Triggers['tr_cep'] = True
                except:
                    print('Digite um CEP')


            #Validando E-MAIL
            if flag_email == False:
                if self.values['email'] != '':
                    email = set_email(self.values['email'])
                    if email:
                        flag_email = True
                        list_Triggers['tr_email'] = True
                        print(flag_email)
            if flag_email == 1 and self.values['email'] == '':
                flag_email = False



            #Valida nome
            if flag_Name == False:
                if self.values['name'] != '':
                    vl_name = self.values['name']
                    name = set_Name(vl_name.strip())
                    if name == True:
                        flag_Name = True
                        list_Triggers['tr_name'] = True
            if self.values['name'] == '' and flag_Name == True:
                flag_Name = False


            #valida CPF
            if self.values['cpf'] != '':
                try:
                    valida_cpf(self.values['cpf'])
                    list_Triggers['tr_cpf'] = True
                except:
                    pass
            else:
                list_Triggers['tr_cpf'] = False

                #telefone
            if self.values['tel'] != '':
                try:
                    set_Tell_fixo(self.values['tel'])
                    list_Triggers['tr_phone'] = True
                except:
                    pass
            else:
                list_Triggers['tr_phone'] = False




            if evento == 'Salvar':
                i = False
                for key, vl_li in list_Triggers.items():
                    if list_Triggers[key] == True:
                        print(key,list_Triggers[key])
                        i = True
                    else:
                        i = False
                        break
                if i:
                    try:
                        salvar = {
                            'Nome': self.values['name'],
                            'Idade': self.values['age'],

                            'CPF': self.values['cpf'],
                            'Telefone': self.values['tel'],

                            'E-mail': self.values['email'],

                            'CEP': self.values['cep'],
                            'Bairro': self.values['bairro'],
                            'Rua': self.values['rua'],
                            'N': self.values['number']
                        }
                        arquivo = open('Cadastro.txt','a')

                        arquivo.write('[')
                        for key, vl_sv in salvar.items():
                            if key != 'N:':
                                arquivo.write('{')
                                arquivo.write('{0}:"{1}"'.format(key,salvar[key]))
                                arquivo.write('},')
                            else:
                                arquivo.write('{')
                                arquivo.write('{0}:"{1}"'.format(key, salvar[key]))
                        arquivo.write('}]')
                        arquivo.write('\n')
                        arquivo.close()
                    except:
                        pass












tela = Tela_Cadastro()

