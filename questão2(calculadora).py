# Questão 2 - CALCULADORA

# Estrutura de repetição para caso o usuário queira continuar os cálculos
continue_math = "sim"
while continue_math == "sim":
    sign = input('Digite um dos operadores desejados [+, -,*, /]:')

    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
# Operação de adição
    if sign == '+':
        print('{} + {} = '.format(n1, n2))
        print(n1 + n2)
        continue_math = input(
            "Deseja continuar usando a calculadora (sim ou não):")
# Operação de subtração
    elif sign == '-':
        print('{} - {} = '.format(n1, n2))
        print(n1 - n2)
        continue_math = input(
            "Deseja continuar usando a calculadora (sim ou não):")
# Operação de multiplicar
    elif sign == '*':
        print('{} * {} = '.format(n1, n2))
        print(n1 * n2)
        continue_math = input(
            "Deseja continuar usando a calculadora (sim ou não):")
# Operação de divisão
    elif sign == '/':
        print('{} / {} = '.format(n1, n2))
        print(n1 / n2)
        continue_math = input(
            "Deseja continuar usando a calculadora (sim ou não):")
else:
    print("Fim das calculations")
