while True:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operador = input("Digite um operador (+,-,/,*): ")
    resultado1 = (num1 + num2)
    resultado2 = (num1 - num2)
    resultado3 = (num1 / num2)
    resultado4 = (num1 * num2)
    operador_val = ["+", "-", "/", "*"]
    
    if operador not in operador_val:
        print("Este não é um operador válido, tente novamente.")
        continue

    if operador == "+":
        print(resultado1)
    elif operador == "-":
        print(resultado2) 
    elif operador == "/":
        print(resultado3)
    else:
        print(resultado4)

    pergunta = input("Deseja tentar novamente? ").lower() 
    if pergunta == "n":
        break