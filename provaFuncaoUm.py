notas = []
while True:
    validar = int(input("Você quer adicionar uma nota de aluno? (1 = sim / 2 = não):"))
    if validar == 1:
        nota = float(input("Digite a nota do aluno:"))
        notas.append(nota)
    elif validar == 2:
        break
    else:
        print("Resposta inválida")
def calcularMedia (a):
    soma = sum(a)
    media = soma / len(a)
    if media <= 6.9:
        return "Média = {}. REPROVADO".format(media)
    elif media >= 7 and media <= 9.9:
        return "Média = {}. PARABÉNS. VOCÊ FOI APROVADO".format(media)
    else:
        return "Média = {}. PARABÉNS. SUA MÉDIA É 10".format(media)

print(f"A situação do aluno é: {calcularMedia(notas)}")

