tab=[32, 16, 5, 8, 24, 7]
i=0
with open('zad13.txt','w') as file:
    while i<len(tab):
        x=str(tab[i])
        i+=1
        file.write(f'{x}\n')
    
