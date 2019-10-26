x=[15,8,31,47,2,19]
<<<<<<< HEAD

suma=0
for i in x:
    if i%2!=0:
        suma+=i
np=0
for i in x:
    if i%2!=0:
        np+=1
        
    
wynik=suma/np #do poprawienia n - liczby parzyste
=======
suma=0
n=len(x)
for i in x:
    if i%2!=0:
        suma+=i
    
wynik=suma/n #do poprawienia n - liczby parzyste
>>>>>>> d7ab3a407cd80c70004ecb7b1a287da8457ea5a3
print(f'Średnia arytmetyczna wynosi {wynik}')