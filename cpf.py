#VALIDAR CPF com python - primeiro digito
import re
import sys

entrada = input("Digite seu cpf: ")
entrada_seq = entrada == entrada[0] * len(entrada) 
if entrada_seq:
    print(f"Você enviou dados em sequência: {entrada}") 
    sys.exit()

cpf_enviado = re.sub(r"[^0-9]", "", entrada) 
print(cpf_enviado)
#cpf_enviado = "068.733.814-03".replace(".", "").replace("-", "")
digitos9 = cpf_enviado[:9]
contador_regressivo1 = 10 

resultado_digito1 = 0
for digito1 in digitos9:
    resultado_digito1 += int(digito1) * contador_regressivo1
    contador_regressivo1 -= 1 

digito1 = (resultado_digito1 * 10) % 11 
digito1 = digito1 if digito1 <= 9 else 0
print(digito1) 

#------------segundo digito----------------
digitos10 = digitos9 + str(digito1) 
contador_regressivo2 = 11

resultado_digito2 = 0
for digito2 in digitos10:
    resultado_digito2 += int(digito2) * contador_regressivo2
    contador_regressivo2 -= 1 

digito2 = (resultado_digito2 * 10) % 11 
digito2 = digito2 if digito2 <= 9 else 0
print(digito2)

cpf_valido = digitos9 + str(digito1) + str(digito2) 

if cpf_enviado == cpf_valido:
    print(f"{cpf_enviado} CPF VÁLIDO!") 
else:
    print(f" {cpf_enviado} CPF INVÁLIDO!")
