# Armazenamento dos dados na lista
aluno = []
nota = []
prs = []
resume = []
for c in range(0, 10):
    aluno.append(str(input('Aluno: ')))  # Elemento 0
    nota.append(float(input('Nota: ')))  # Elemento 1
    prs.append(float(input('Presença: ')))  # Elemento 2
    list = [(aluno[c]), nota[c], prs[c]]    # Agrupamento das listas
    resume.append(list)

print("-=-"*30)


# Função para checar aprovação do aluno
def aprova(resume):
    for a in resume:
        if a[1] >= 7 and a[2] >= 75:
            print(f'{a[0]} está APROVADO com nota {a[1]} e prensença de {a[2]}% ')
        else:
            print(f'{a[0]} está REPROVADO com nota {a[1]} e presença de {a[2]}% ')
    return aprova


aprova(resume)
