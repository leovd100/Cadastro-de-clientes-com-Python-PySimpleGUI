import PySimpleGUI as sg

class Screen:
    def __init__(self):
        layout = [
            [sg.Button('Todos'),sg.Button('Nome')],
            [sg.Output(size=(200,10))]



        ]
        self.screen = sg.Window('Tela de consulta', layout)



        while True:

            data = []
            evento, self.values = self.screen.Read()
            if evento == 'Todos':
                try:
                    with open('Cadastro.txt') as arquivo:
                        file = arquivo.read()[1:len(arquivo.read())-2]
                        lista = file.split(',')


                        # for x in lista:

                        dicionario_lista = {'nome':lista[0][lista[0].find(':')+1:-1]
                                            ,'idade':lista[1][lista[1].find(':')+1:-1]
                                            ,'cpf':lista[2][lista[2].find(':')+1:-1]
                                            ,'telefone':lista[3][lista[3].find(':')+1:-1]
                                            ,'email':lista[4][lista[4].find(':')+1:-1]
                                            ,'cep':lista[5][lista[5].find(':')+1:-1]
                                            ,'bairro':lista[6][lista[6].find(':')+1:-1]
                                            ,'rua':lista[7][lista[7].find(':')+1:-1]
                                            ,'numero':lista[8][lista[8].find(':')+1:-1]}

                        for key,val in dicionario_lista.items():
                            print(key,end='                   ')
                        print('\n')
                        for key, val in dicionario_lista.items():
                            print(val,end='    ')




                except:
                    print('Sem arquivo')




lf = Screen()