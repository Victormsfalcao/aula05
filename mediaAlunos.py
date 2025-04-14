soma = 0
qtd = 1
qtdAlunos = int(input("Insira a quantidade de alunos: "))
while qtd <= qtdAlunos:
    num = float(input("Insira a nota : "))
    qtd +=1
    soma = soma + num
media = soma / qtdAlunos
print(f"A turma tem {qtdAlunos} alunos, e a média de notas é {media} ")