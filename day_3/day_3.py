# https://adventofcode.com/2022/day/3

p1=""
p2=""
total=0

with open("e:/code/advent_code/2022/day_3/input.txt") as archivo: # usar la localizacion de tu archivo
    for linea in archivo:
        found=False
        p1=linea[0:int((len(linea)-1)/2)]
        p2=linea[int((len(linea)-1)/2):len(linea)-1]
        for n in p1:                                        # we go through the first half of the string
            if not found:
                for m in p2:                                # we go through the second half of the string
                    if n==m and not found:
                        print(n)                            # this is just to make it more visual
                        if(n.isupper()):
                            total=total+ord(n)-38           # we use the ascii values of each character
                            print(ord(n)-38)                # this is just to make it more visual
                        else:
                            total=total+ord(n)-96           # we use the ascii values of each character
                            print(ord(n)-96)                # this is just to make it more visual
                        found=True                          # to make sure that not a single repeated item is twice in the same pocket

print("total: ",total)


# here starts part 2

group=[]
id=0
total_2=0

with open("e:/code/advent_code/2022/day_3/input.txt") as archivo: # usar la localizacion de tu archivo
    for linea in archivo:
        found=False
        group.append(linea[:len(linea)-1])
        id=id+1                                 # to know when the groups of 3 are done
        print("id: ", id)                       # this is just to make it more visual
        if(id%3==0):
            print(group[0])
            print(group[1])
            print(group[2])
            for n in group[0]:
                if not found:
                    for m in group[1]:
                        if n==m and not found:
                            for o in group[2]:
                                if not found and o==n:
                                    print(n)                                # this is just to make it more visual
                                    if(n.isupper()):
                                        total_2=total_2+ord(n)-38           # we use the ascii values of each character
                                        print(ord(n)-38)                    # this is just to make it more visual
                                    else:
                                        total_2=total_2+ord(n)-96           # we use the ascii values of each character
                                        print(ord(n)-96)                    # this is just to make it more visual
                                    found=True
                                    group=[]


print("total_2: ", total_2)


                        

