numbers = []
suma = []
with open('numbersinrows.txt','r') as fi:
    for line in fi:
        line =line.strip('\n')
        line =line.split(',')
        for liczba in line:
            numbers.append(liczba)
for cyfra in numbers:
    suma.append(int(cyfra))
print(f'Ilosc liczb = {len(numbers)}, a ich suma = {sum(suma)}')                
                
        