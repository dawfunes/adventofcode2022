# https://adventofcode.com/2022/day/5

lineas=[]
moving=False
stacks=0
crates_to_move=0

with open("E:/code/advent_code/2022/day_5/input.txt") as archivo: #usar la localizacion de tu archivo
    for linea in archivo:
        if(linea!="\n"):
            if(not moving):
                lineas.append(linea)
                if(linea[1]=="1"):
                    lineas.pop(len(lineas)-1)
                    for m in range(100):
                        n=m*4+1
                        if n>len(linea)-1:
                            break
                        else:
                            stacks=stacks+1
                            locals()["stack_"+linea[n]]=[]
                            for crate in lineas:
                                if crate[n]!=" ":
                                    locals()["stack_"+linea[n]].append(crate[n])
                            locals()["stack_"+linea[n]]=locals()["stack_"+linea[n]][::-1]       # We invert the array so the top crate will be in last position instead of first
            else:
                div_instruction=linea[:len(linea)-1].split(" ")
                for m in range(int(div_instruction[1])):
                    locals()["stack_"+div_instruction[5]].append(locals()["stack_"+div_instruction[3]][len(locals()["stack_"+div_instruction[3]])-1])
                    locals()["stack_"+div_instruction[3]].pop(len(locals()["stack_"+div_instruction[3]])-1)
        else:
            moving=True                                                     # we start "moving" whenever the instructions start

solution=""

for m in range(stacks):
    print(str(m+1), " - ",locals()["stack_"+str(m+1)])
    solution=solution+locals()["stack_"+str(m+1)][len(locals()["stack_"+str(m+1)])-1]

print("solution: ",solution)

# Here starts part 2

lineas=[]
moving=False
stacks=0
crates_to_move=0

with open("E:/code/advent_code/2022/day_5/input.txt") as archivo: #usar la localizacion de tu archivo
    for linea in archivo:
        if(linea!="\n"):
            if(not moving):
                lineas.append(linea)
                if(linea[1]=="1"):
                    lineas.pop(len(lineas)-1)
                    for m in range(100):
                        n=m*4+1
                        if n>len(linea)-1:
                            break
                        else:
                            stacks=stacks+1
                            locals()["stack_"+linea[n]]=[]
                            for crate in lineas:
                                if crate[n]!=" ":
                                    locals()["stack_"+linea[n]].append(crate[n])
                            locals()["stack_"+linea[n]]=locals()["stack_"+linea[n]][::-1]       # We invert the array so the top crate will be in last position instead of first
            else:
                div_instruction=linea[:len(linea)-1].split(" ")
                locals()["stack_"+div_instruction[5]]=locals()["stack_"+div_instruction[5]]+locals()["stack_"+div_instruction[3]][-1*int(div_instruction[1]):]
                locals()["stack_"+div_instruction[3]]=locals()["stack_"+div_instruction[3]][:len(locals()["stack_"+div_instruction[3]])-int(div_instruction[1])]
        else:
            moving=True                                 # we start "moving" whenever the instructions start

solution=""

for m in range(stacks):
    print(str(m+1), " - ",locals()["stack_"+str(m+1)])
    solution=solution+locals()["stack_"+str(m+1)][len(locals()["stack_"+str(m+1)])-1]

print("solution: ",solution)                                                                        # All this last area is just to print the solution so it's easier to see