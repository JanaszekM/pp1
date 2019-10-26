x=int(input('podaj wysokość prostokąta: '))
y=int(input('podaj szerokość prostokąta: '))
print(y*'*')
i=0
while i<(x-2):
    i+=1
    print('*',(y-4)*' ', '*')
print(y*'*')
