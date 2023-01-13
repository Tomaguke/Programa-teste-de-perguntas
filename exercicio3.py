# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

contador = 0
resposta_1 = perguntas[0]['Resposta']
resposta_2 = perguntas[1]['Resposta']
resposta_3 = perguntas[2]['Resposta']


lista_1 = (perguntas[0]['Opções'])
lista_2 = (perguntas[1]['Opções'])
lista_3 = (perguntas[2]['Opções'])

print(perguntas[0]['Pergunta'])
print('As opcoes são',perguntas[0]['Opções'])

resposta = 0
contador = 0
Resposta_incorreta = True
while Resposta_incorreta:
    resposta = str(input('Resposta: '))
    i = 0
    if resposta == resposta_1:
            print('Resposta Correta!!!')
            contador += 1
            Resposta_incorreta = False
    else:
        while i < len(lista_1):
            if resposta != perguntas[0]['Opções'][i]:
                i+= 1
                continue
            elif resposta == perguntas[0]['Opções'][i]:
                print('Resposta Incorreta')
                Resposta_incorreta = False
                break
        if i == len(lista_1):
            print('Digite apenas uma das opcoes acima')
            
                
                
                
print(perguntas[1]['Pergunta'])
print('As opcoes são',perguntas[1]['Opções'])

resposta = 0
Resposta_incorreta = True
while Resposta_incorreta:
    resposta = str(input('Resposta: '))
    i = 0
    if resposta == resposta_2:
            print('Resposta Correta!!!')
            contador += 1
            Resposta_incorreta = False
    else:
        while i < len(lista_2):
            if resposta != perguntas[0]['Opções'][i]:
                i+= 1
                continue
            elif resposta == perguntas[0]['Opções'][i]:
                print('Resposta Incorreta')
                Resposta_incorreta = False
                break
        if i == len(lista_2):
            print('Digite apenas uma das opcoes acima')

print(perguntas[2]['Pergunta'])
print('As opcoes são',perguntas[2]['Opções'])

resposta = 0
Resposta_incorreta = True
while Resposta_incorreta:
    resposta = str(input('Resposta: '))
    i = 0
    if resposta == resposta_3:
            print('Resposta Correta!!!')
            contador += 1
            Resposta_incorreta = False
    else:
        while i < len(lista_3):
            if resposta != perguntas[0]['Opções'][i]:
                i+= 1
                continue
            elif resposta == perguntas[0]['Opções'][i]:
                print('Resposta Incorreta')
                Resposta_incorreta = False
                break
        if i == len(lista_3):
            print('Digite apenas uma das opcoes acima')
            
print(f'Voce acertou {contador} de {len(perguntas)} Perguntas')           
        
                
'''resposta = 0

while resposta != resposta_2:
    resposta = str(input('Resposta: '))
    match resposta:

            case '25':
                print('Resposta Correta!!')
                contador += 1
            case '55':
                print('Resposta Incorreta')
            case '10':
                print('Resposta Incorreta')
            case '51':
                print('Resposta Incorreta')
            case _:
                print('Digite apenas uma das opcoes acima')
'''



'''resposta = 0
while resposta != 1 or 3 or 4 or 5:
    resposta = input('Resposta: ')
    
    match resposta:

            case 1:
                print('Resposta Incorreta')
            case 3:
                print('Resposta Incorreta')
            case 4:
                print('Resposta Correta!!')
                contador += 1
            case 5:
                print('Resposta Incorreta')
            case _:
                print('Digite apenas uma das opcoes acima')
                
print(perguntas[1]['Pergunta'])
print('As opcoes são',perguntas[1]['Opções'])
                
while resposta != 25 or 55 or 10 or 51:
    resposta = input('Resposta: ')
    
    match resposta:

            case 25:
                print('Resposta Correta!!')
                contador += 1
            case 55:
                print('Resposta Incorreta')
            case 10:
                print('Resposta Incorreta')
            case 51:
                print('Resposta Incorreta')
            case _:
                print('Digite apenas uma das opcoes acima')
                
while resposta != 4 or 5 or 2 or 1:
    resposta = input('Resposta: ')
    
    match resposta:

            case 4:
                print('Resposta Correta!!')
                contador += 1
            case 5:
                print('Resposta Incorreta')
            case 2:
                print('Resposta Incorreta')
            case 1:
                print('Resposta Incorreta')
            case _:
                print('Digite apenas uma das opcoes acima')'''
        