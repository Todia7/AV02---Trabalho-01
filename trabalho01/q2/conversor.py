def ConversorParaFahrenheit (temperaturaCelsius):
    resultado = (temperaturaCelsius * 9/5) + 32
    return resultado


def ConversorParaCelsius (temperaturaFahrenheit):
    resultado = (temperaturaFahrenheit - 32) * 5/9
    return resultado