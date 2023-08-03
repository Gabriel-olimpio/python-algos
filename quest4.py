# Listas 1 e 2
print("="*20)
list1 = [12, 55, 7, 4, 8, 15, 2, 63, 2, 5]
print('Lista 1: ', list1)

list2 = [9, 4, 86, 22, 21, 3, 67, 27, 47, 78]
print('Lista 2:', list2)
print("="*20)

# Junção da lista 1 e 2 para formar a 3
list3 = []
for item in range(len(list1)):
    list3.append(list1[item])
    list3.append(list2[item])
print('A intercalação entre as listas 1 e 2 = ', list3)
print("="*20)


# Função para mostrar ocorrência e multiplos na lista
def indice(list3):
    for item in list3:
        n = int(input('Digite um número para saber o indice: '))
        if (n % (list3[item])) == 0:
            return print('Ocorrências encotradas: ', list3.count(n), '\nMúltiplos: ', list3.count(n))
        else:
            return print('Ocorrências encontradas: ', list3.count(n), '\nNão obtivemos múltiplos na lista')


indice(list3)
