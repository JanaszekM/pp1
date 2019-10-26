liczba=str(input('Podaj liczbę: '))
slownie=['zero','jeden','dwa','trzy','cztery','pięć','sześć','siedem','osiem','dziewięć']
print(f'{liczba} -',end=" ")
for i in range(0,len(liczba)):
    n=int(liczba[i])
    print(slownie[n],end=' ')