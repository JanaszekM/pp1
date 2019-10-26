x=[15,8,31,47,2,19]

suma=0
for i in x:
    if i%2!=0:
        suma+=i
np=0
for i in x:
    if i%2!=0:
        np+=1
        
    
wynik=suma/np #do poprawienia n - liczby parzyste
print(f'Średnia arytmetyczna wynosi {wynik}')