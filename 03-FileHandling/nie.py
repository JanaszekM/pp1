import re
x=[]

with open('numbers.txt','r') as file:
    for line in file:
        x.append(line.strip().split(','))

print(sorted(x))