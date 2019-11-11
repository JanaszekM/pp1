from random import randrange
 

def rzuckostka():
    sum=0
    i=0
     
    while i<3:
        x=randrange(1,7)
        print(x, end=' ')
        sum+=x
        i+=1
    print(f'\nSuma oczek: {sum}')
rzuckostka()
     
 