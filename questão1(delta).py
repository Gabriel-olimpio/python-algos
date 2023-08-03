# Questão 1 - DELTA

print("--" * 25)
print('Identifique os coeficientes para A, B, C, D')
print("--" * 25)

# Input's para os coeficientes A, B, C
c1 = float(input("Escolha um coeficiente para a:"))  # a
c2 = float(input("Escolha um coeficiente para b:"))  # b
c3 = float(input("Escolha um coeficiente para c:"))  # c

# Calculo do delta
delt = (c2**2)-4 * c1*c3
print('Delta = {}'.format(delt))

print('--' * 35)

# Resultados
print('Os resultados são os seguintes:')

if c1 == 0:
    print('O coeficiente "a" é somente aceito se for [a < 0 ou a > 0]')

    print('Não há raízes possíveis')
elif (delt == 0):
    print('Um valor real')
    print('Delta = 0')
elif (delt >= 0):
    print('Dois valores reais')
    print('Delta > 0')
elif (delt <= 0):
    print('Não contém valores reais')
    print('Delta < 0')
else:
    print('End')

# Raízes
print('--' * 35)

print(' Raízes: ')
a1 = (- c2 + (delt ** (1 / 2))) / (2 * c1)
a2 = (- c2 + (delt ** (1 / 2))) / (2 * c1)
print('Primeira Raíz = {}'.format(a1))
print('Segunda Raíz = {}'.format(a2))

print('--' * 35)
