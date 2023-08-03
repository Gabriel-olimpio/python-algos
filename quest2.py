# Lista de Jogadores
players = ['Neymar', 'Richarlison', 'Vini-Jr', 'Raphinha', 'Antony',
           'Pedro', 'Paquetá', 'Rodrygo', 'Marquinhos', 'Fred', 'Casemiro']

# Lista de Taxas de acerto
acerto = [99.9, 90.7, 99.8, 87.8, 78.4, 87.6, 88.5, 11.6, 55.7, 76.2, 94.2]

# Lista em que será colocado [(Taxa), (Jogador)] e ficará de forma decrescente
ordem = []
for p in range(0, 11):
    list = [(acerto[p]), (players[p])]
    ordem.append(list)
    ordem.sort()

print("-=-"*50)
print('A ordem de cobrança de penaltis é:\n', sorted(ordem, reverse=True))
print("-=-"*50)
