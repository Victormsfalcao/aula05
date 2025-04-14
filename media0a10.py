resposta = "s"
while resposta == "s":
    nota1 = float(input("Insira a primeira nota: "))
    while nota1 < 0 or nota1 >10:
        nota1 = float(input("Insira a primeira nota: "))

    nota2 = float(input("Insira a segunda nota: "))

    while nota2 < 0 or nota2 >10:
        nota2 = float(input("Insira a segunda nota: "))

    media = (nota1 + nota2)/2
    print(media)
    resposta = input("Deseja realizar novo calculo? ").lower()


