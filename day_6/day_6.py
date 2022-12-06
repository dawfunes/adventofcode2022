# https://adventofcode.com/2022/day/6

signal=""

with open("E:/code/advent_code/2022/day_6/input.txt") as archivo: #usar la localizacion de tu archivo
    for linea in archivo:
        signal+=linea[:len(linea)-1]                              # We save the information in a string 'signal'

done=False

for n in range(len(signal)):
    print(signal[n:n+4])                 # This will show us the strings of 4 that we are checking            
    if not done:                         # Constantly checking if we have already found it so we can stop the loop
        cont=0
        for m in signal[n:n+4]:
            if signal[n:n+4].count(m)==1:
                cont+=1
            else:
                break                    # If the condition is not fulfilled, the loop will stop
            if cont==4:
                solution=n
                done=True                
    else:
        break

print(solution+4)                        # Since we are checking from the front we have to add 4

# Here starts part 2
# Now we are supposed to do the exact same but with 14 instead of 4
# We just copy and paste the code we already have developed and adjust the values

done=False                               # We reset the value of 'done'

for n in range(len(signal)):
    print(signal[n:n+14])                # This will show us the strings of 4 that we are checking            
    if not done:                         # Constantly checking if we have already found it so we can stop the loop
        cont=0
        for m in signal[n:n+14]:
            if signal[n:n+14].count(m)==1:
                cont+=1
            else:
                break                    # If the condition is not fulfilled, the loop will stop
            if cont==14:
                solution=n
                done=True                
    else:
        break

print(solution+14)                       # Since we are checking from the front we have to add 14