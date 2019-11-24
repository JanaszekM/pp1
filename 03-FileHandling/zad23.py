import re
suma=[]

with open('land.txt','r') as file:
    liczby=re.findall('\d.*?',file.read())
    for i in liczby:
        suma.append(int(i))
    
    print(sorted(suma))
    