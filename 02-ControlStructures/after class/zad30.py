x=str
pin='0010'
i=0
proby=3
while i<3:
    i=i+1
    proby-=1
    if x != pin:
        x=str(input('Podaj kod PIN:'))
    if x==pin:
       print('Kod PIN poprawny')
       break
    if x!=pin:
        print(f'Kod PIN niepoprawny. Możliwe próby: {proby}')
    
    if i==3:
        print('Kart płatnicza zostaje zablokowana')
          
    