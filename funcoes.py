def multiplicacao(*args):
    total = 1 
    for num in args:
        total *= num
    return total

resultado = multiplicacao(2,4,5,1)
print(resultado)

#--------------------------------------------------
def par_impar(numero):
    if numero % 2 == 0:
        return ("É par!") 
    else:
        return("É ímpar!") 
     

print(par_impar(5))
print(par_impar(6)) 

#--------------------------------------------------------------------

def criar_multiplicador(multiplicador):
    def multiplicar(num):
        return num * multiplicador 
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4) 

print(duplicar(2)) 
print(triplicar(2))
print(quadruplicar(2))

