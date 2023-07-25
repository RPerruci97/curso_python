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

while True:
    print("Pergunta: quanto é 2+2?") 
    print("Opções: \n", 1, 3, 4, 5) 
    resposta1 = int(input("Resposta - escolha o número correto dentre as opções: ")) 

    if resposta1 == 4:
        print("Acertou!") 
    else:
        print("Errou")
   
    print("Pergunta: quanto é 5x5?") 
    print("Opções: \n", 10, 25, 55, 5) 
    resposta2 = int(input("Resposta - escolha o número correto dentre as opções: ")) 

    if resposta2 == 25:
        print("Acertou!") 
    else:
        print("Errou")
    
    
    print("Pergunta: quanto é 10/2?") 
    print("Opções: \n", 10, 4, 2, 5) 
    resposta3 = int(input("Resposta - escolha o número correto dentre as opções: ")) 

    if resposta3 == 5:
        print("Acertou!") 
    else:
        print("Errou ")
    break

#------------------------outra forma de resolução 

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()


print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')