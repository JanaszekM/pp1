from random import randrange
y=[]
even=[]
odd=[]
print('Dla 1000 liczb losowych z przedziału <1,50>: ')
def clown():
    for i in range(0,1000):
        x=randrange(1,51)
        y.append(x)
        
    for liczby in y:
        if liczby%2==0:
            even.append(liczby)
        else:
            odd.append(liczby)
    print(f'Liczby parzyste: {(len(even)/1000)*100:.2f}%')
    print(f'Liczby nieparzyste: {(len(odd)/1000)*100:.2f}%')
clown()

