# https://adventofcode.com/2022/day/1#part2

elfos=[]
suma=0

with open("e:/code/advent_code/2022/day_1/input.txt") as archivo: #usar la localizacion de tu archivo
    for linea in archivo:
        if linea=="\n":
            elfos.append(suma)
            suma=0
        else:
            aux=int(linea)
            suma=suma+aux

print(elfos)
print("El elfo con más calorias tiene:")
print(max(elfos))

# Aquí hacemos la parte 2

top3=0

for n in range(3):
    aux=max(elfos)
    elfos.remove(max(elfos))
    top3=top3+aux

print("El top 3 suman estas calorias:")
print(top3)

