senhaCorreta = 123456
tentativas = 1
mensagem = "Senha Bloqueada"
while tentativas <=3:
    senha = int(input("Digite a senha: "))
    if senha == senhaCorreta:
       mensagem = "Senha correta"
       break
    tentativas +=1
print(mensagem)

