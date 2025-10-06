# Questão 4 - Verificador de Números Pares e Ímpares
# Crie uma função que receba um número inteiro e retorne se ele é par ou ímpar.

numero = int(input("Digite um número: "))

def verificar_par_impar(numero_para_verificar):
    if numero_para_verificar % 2 == 0:
        return "Par"
    else:
        return "Ímpar"
    
resultado = verificar_par_impar(numero)

print(f"O número {numero} é {resultado}.")