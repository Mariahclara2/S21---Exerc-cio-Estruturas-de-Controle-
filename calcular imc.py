# Função para calcular o IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Função para classificar o IMC
def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25.0 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"

# Entrada de dados
peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

# Cálculo do IMC
imc = calcular_imc(peso, altura)

# Exibição do resultado
print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificar_imc(imc)}")
