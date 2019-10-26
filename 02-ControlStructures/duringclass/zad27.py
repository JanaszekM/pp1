h=int(input('podaj wysokość trójkąta'))
x=int(input('podaj długość trójkąta'))

i=0
h=0
while i<=(x/2):
    i+=1
    h+=1
    print(h*'*')
while i<(x):
    i+=1
    h-=1
    print((h)*'*')
