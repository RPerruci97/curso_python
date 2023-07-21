def multiplicacao(*args):
    total = 1 
    for num in args:
        total *= num
    return total

resultado = multiplicacao(2,4,5,1)
print(resultado)

def par_impar(numero):
    if numero % 2 == 0:
        return ("É par!") 
    else:
        return("É ímpar!") 
     

print(par_impar(5))
print(par_impar(6))


