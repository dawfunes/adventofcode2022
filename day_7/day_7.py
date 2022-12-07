# https://adventofcode.com/2022/day/7

from anytree import Node, RenderTree

current_directory="main"
main=Node("main")
size_main=0

with open("E:/code/advent_code/2022/day_7/input.txt") as archivo: #usar la localizacion de tu archivo
    for linea in archivo:
        command = False
        if linea[0]=="$":
            command = True
        if command:
            if linea[2]+linea[3]=="cd":
                if linea[5:len(linea)-1]=="..":
                    current_directory=locals()[current_directory].parent.name
                elif linea[5]=="/":
                    current_directory="main"
                else:
                    current_directory=linea[5:len(linea)-1]
        else:
            if linea[0:3]=="dir":
                directorio=linea[4:len(linea)-1]
                locals()[directorio]=Node(directorio,parent=locals()[current_directory])
                locals()["size_"+directorio]=0
            else:
                size=""
                for n in linea:
                    if n == " ":
                        locals()["size_"+current_directory]+=int(size)
                        if locals()[current_directory].is_leaf:
                            aux=locals()[current_directory].parent.name
                            while locals()[aux].is_leaf:
                                locals()["size_"+aux]+=locals()["size_"+current_directory]
                                aux=locals()[aux].parent.name
                        break
                    # EL PROBLEMA ESTA AQUI
                    else:
                        size+=n

            
for pre, fill, node in RenderTree(main):
    print("%s%s" % (pre, node.name))

