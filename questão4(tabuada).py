# Questão 4 - TABUADA

# Input do valor para tabuada
table = int(input('Tabuada de: '))

# Input's para inicio e fim da tabuada
i = int(input('Iniciar em:'))
f = int(input('Terminar em:'))

print('Tabuada de {} começando em {} e finalizando em {}'.format(table, i, f))

# Estrutura de repetição e cálculos
x = i
while x <= f:
    print('{} x {} = {}'.format(table, x, table*x))
    x += 1
else:
    print('Eis a tabuada de {}'.format(table))
