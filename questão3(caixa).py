#  Questão 3 - LOJA (Caixa registradora)

total = 0
value = 0
Nproduct = 1
cash = 0

# Nome da Loja
print("-" * 20)
print("Loja dos Vitoriosos")
print("-" * 20)

# Estutura de Repetição para os produtos
while True:
    value = int(input('Product {}: $ '.format(Nproduct)))
    if value == 0:
        break
    else:
        total = total + value
        Nproduct = Nproduct + 1

# Total e Troco
print('Total: ${} '.format(total))
cash = int(input('Dinheiro: $ '))
cashback = cash - total
print('Troco: ${}'.format(cashback))

# Fim do Programa
print("-" * 25)
print("Obrigado pela preferência!")
print("-" * 25)
