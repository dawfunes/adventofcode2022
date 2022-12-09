# https://adventofcode.com/2022/day/7

from anytree import Node, RenderTree

current_directory="main"
main=Node("main")
size_main=0

uwu=0
print(uwu)

for linea in open("E:/code/advent_code/2022/day_7/input.txt"):        #usar la localizacion de tu archivo
    uwu+=1
    print(uwu)
    if linea[0]=="$":
        command = True
    else:
        command = False
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
                if n == " ": # You can easily optimize this with a split and selecting the first element
                    locals()["size_"+current_directory]+=int(size)
                    if not locals()[current_directory].is_root:
                           
                        aux=locals()[current_directory].parent.name
                           
                        while True:
                            locals()["size_"+aux]+=int(size)
                            if locals()[aux].is_root:
                                break
                            else:
                                aux=locals()[aux].parent.name
                    break
                else:
                    size+=n
storage=[]
total=0
for pre, fill, node in RenderTree(main):
    print("%s%s" % (pre, node.name))
    storage.append(node.name)
    if locals()["size_"+node.name]<=100000:
        total+=1

print(storage)
print(total)




