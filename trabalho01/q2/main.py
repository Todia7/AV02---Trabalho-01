# Q2 - Conversor de Temperatura
# Conversão entre Celsius e Fahrenheit
# Obrigração: criar um arquivo conversor.py e importar as funções

import conversor

print("Conversor de Temperatura")
print("1. Celsius para Fahrenheit")
print("2. Fahrenheit para Celsius")
opcao = int(input("Escolha uma opção (1 ou 2): "))

if opcao == 1:
    celsius = float(input("Digite a temperatura em Celsius: "))
    converter_para_fahrenheit = conversor.ConversorParaFahrenheit(celsius)
    print(f"{celsius} graus Celsius é igual a {converter_para_fahrenheit:.2f} graus Fahrenheit.")
elif opcao == 2:
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    converter_para_celsius = conversor.ConversorParaCelsius(fahrenheit)
    print(f"{fahrenheit} graus Fahrenheit é igual a {converter_para_celsius:.2f} graus Celsius.")
else:
    print("Opção inválida.")