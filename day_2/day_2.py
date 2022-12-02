# https://adventofcode.com/2022/day/2#part2

lineas=[]
score=0
yours=0
status=0

with open("e:/code/advent_code/2022/day_2/input.txt") as archivo: #usar la localizacion de tu archivo
    for linea in archivo:
        if(linea[2]=="X"):
            yours=1
            if(linea[0]=="A"):
                status=3
            elif(linea[0]=="B"):
                status=0
            else:
                status=6
        elif(linea[2]=="Y"):
            yours=2
            if(linea[0]=="A"):
                status=6
            elif(linea[0]=="B"):
                status=3
            else:
                status=0
        else:
            yours=3
            if(linea[0]=="A"):
                status=0
            elif(linea[0]=="B"):
                status=6
            else:
                status=3
        score=score+yours+status

print("La score final es: ",score)


# Here starts part 2

score=0

with open("e:/code/advent_code/2022/day_2/input.txt") as archivo: #usar la localizacion de tu archivo
    for linea in archivo:
        if(linea[2]=="X"):
            status=0
            if(linea[0]=="A"):
                yours=3
            elif(linea[0]=="B"):
                yours=1
            else:
                yours=2
        elif(linea[2]=="Y"):
            status=3
            if(linea[0]=="A"):
                yours=1
            elif(linea[0]=="B"):
                yours=2
            else:
                yours=3
        else:
            status=6
            if(linea[0]=="A"):
                yours=2
            elif(linea[0]=="B"):
                yours=3
            else:
                yours=1
        score=score+yours+status

print("\nLa verdadera score final es: ",score)