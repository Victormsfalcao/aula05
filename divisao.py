
num1 = int(input("Informe o primeiro numero: "))
num2 = int(input("Informe o segundo numero: "))

while num2 == 0:
    num2 = int(input("Informe o segundo numero: "))
    if num2 != 0:
        break
divisao = num1 / num2

print(divisao)