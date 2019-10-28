with open('shoppinglist.txt ','w') as file:
    print('Podaj produkty, które należy kupić')
x=[]
while x!='':
    x=(input('Produkty:'))
    file.write(f'{x}\n')

        


