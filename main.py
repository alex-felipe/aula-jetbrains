# Exemplo de código Python com erros intencionais para identificação pelo SonarQube

def calcula_area_circulo(raio):
    # Falta tratamento para valores negativos
    area = 3.1415 * raio * raio
    return area

def main():
    # Uso de variáveis não utilizadas e código duplicado
    resultado = 0
    resultado = calcula_area_circulo(5)
    print("Área do círculo com raio 5:", resultado)

    resultado = calcula_area_circulo(-3)  # Erro: valor negativo

    if resultado > 0:
        print("Área válida")
    if resultado > 0:  # Código duplicado
        print("Área válida")

    print("Fim do programa")

# Função não usada
def calcula_perimetro_circulo(raio):
    perimetro = 2 * 3.1415 * raio
    return perimetro

# Variável global desnecessária
valor_global = 10

main()
