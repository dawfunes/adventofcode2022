# https://adventofcode.com/2022/day/4#part2

total=0

with open("E:/code/advent_code/2022/day_4/input.txt") as archivo: #usar la localizacion de tu archivo
    for linea in archivo:
        gnomos=linea[:len(linea)-1].split(",")
        if(int(gnomos[0].split("-")[0])-int(gnomos[1].split("-")[0])>=0 and int(gnomos[0].split("-")[1])-int(gnomos[1].split("-")[1])<=0) or (int(gnomos[0].split("-")[0])-int(gnomos[1].split("-")[0])<=0 and int(gnomos[0].split("-")[1])-int(gnomos[1].split("-")[1])>=0):
            total=total+1

print(total)

# here starts part 2

total=0

with open("E:/code/advent_code/2022/day_4/input.txt") as archivo: #usar la localizacion de tu archivo
    for linea in archivo:
        gnomos=linea[:len(linea)-1].split(",")
        if(int(gnomos[0].split("-")[0])-int(gnomos[1].split("-")[1])>=0 and int(gnomos[0].split("-")[1])-int(gnomos[1].split("-")[0])<=0) or (int(gnomos[0].split("-")[0])-int(gnomos[1].split("-")[1])<=0 and int(gnomos[0].split("-")[1])-int(gnomos[1].split("-")[0])>=0):
            total=total+1


print(total)