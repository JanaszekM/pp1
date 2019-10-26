names=['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy', 'Teofil']
longest=0
n=0
for i in range(0,len(names)):
    if len(names[i])>n:
        n=len(names[i])
        longest=names[i]
print(f'Najdłuższe imie: {longest}')
    