import math
x = 8
y = 3
sqrtX = math.sqrt(x) 
print(f'Pierwiastek kwadratowy z {x} wynosi {sqrtX}')
powx=math.pow(x,y)
print(f'Potęga x do y wynosi {powx}')
potega= math.pow(x,1.0/y)
print(potega)
pole=(math.pi)*4**2
print(pole)
def silnia(y):
    i=y
    while y>1:
        y=y-1
        i=i*y
    return i       
print(silnia(y))

calkowita=math.floor(x)
print('xxx')
print(calkowita)