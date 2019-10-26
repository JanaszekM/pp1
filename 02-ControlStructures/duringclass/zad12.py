print('Podaj x')
x=int(input())
print('Podaj y')
y=int(input())
if x<0 or y<0:
    print('{Jedna z podanych liczb posiada wartość ujemną')
if x<0 and y<0:
    print('Obie wartości są ujemne')
if x>0 and y>0:
    print('Obie wartości są dodatnie')
