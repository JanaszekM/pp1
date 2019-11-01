number=[]
even=[]
with open('numbers.txt','r') as f:
    for line in f:
        number.append(int(line))
    for liczba in number:
        if liczba%2==0: 
            even.append(liczba)
with open('evennumber.txt', 'w') as file:
    for x in even:
       file.write('{}\n'.format(str(x)))