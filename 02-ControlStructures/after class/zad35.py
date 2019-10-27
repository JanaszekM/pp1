import math
print('ax2+bx+c=0')
a=int(input('podaj a: '))
b=int(input('podaj b: '))
c=int(input('podaj c: '))

delta= (b**2) -4*a*c
if delta<0:
    print('Brak miejsc zerowych')
elif delta==0:
    mz=-b/2*a
    print(f'Jedyne miejsce zerowe to {mz}')
else:
    pierw=math.sqrt(delta)
    mz1=(-b-pierw)/2*a
    mz2=(-b+pierw)/2*a
    print(f'Miejsca zerowe to {mz1} oraz {mz2}')