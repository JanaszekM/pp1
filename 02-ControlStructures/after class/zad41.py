#x=ilość wprowadzone liczby
x=0
suma=0
tab=''
while tab!=0:
    x+=1
    tab=int(input('podaj liczbe'))
    suma+=tab
srednia=suma/(x-1)
print(f'REZULTAT: Liczb= {x-1}, Suma= {suma}, Średnia= {srednia}.')


