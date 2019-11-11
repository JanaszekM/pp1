imiona=['Janek', 'Ania', 'Wojtek', 'Zosia']
imie='Wojtek'

def jestimie(imie,imiona):
    status=0
    
    print(f'{imiona}')
    
    print(imie)
    if imie in imiona:
        status=1
    else:
        status=0
    if status == 1:
        print('Rezultat: imie jest zawarte w wykazie imion')
    else:
        print('Rezultat: imie nie jest zawarte w wykazie imion')
        
jestimie('Ania',imiona)
