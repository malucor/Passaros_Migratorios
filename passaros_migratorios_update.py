import os
import statistics

id_passaros = []

qtd_passaros = int(input('Digite a quantidade de pássaros que foram avistados: '))

for passaros in range(qtd_passaros):
    passaros = int(input('Digite o ID de cada pássaro observado: '))
    id_passaros.append(passaros)

moda = statistics.multimode(id_passaros)
moda.sort(key=int)
moda = moda[0]

os.system('cls') or None

print(f'ID dos pássaros avistados: \n', id_passaros)
print(f'Pássaro avistado com mais frequência: \n', moda)