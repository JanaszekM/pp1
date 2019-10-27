kwota=int(input('Podaj kwotę w zł: '))

cale5=kwota//5
resztaz5=kwota-(cale5*5)
cale2=resztaz5//2
resztaz2=resztaz5-(cale2*2)
cale1=resztaz2


print(f'kwota {kwota} zł w monetach: ')
print(f'5zł - {cale5} szt')
print(f'2zł - {cale2} szt')
print(f'1zł - {cale1} szt')