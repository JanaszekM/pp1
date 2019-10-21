x=[15,8,31,47,2,19]
suma=0
n=len(x)
for i in x:
    if i%2!=0:
        suma+=i
    
wynik=suma/n #do poprawienia n - liczby parzyste
print(f'Średnia arytmetyczna wynosi {wynik}')