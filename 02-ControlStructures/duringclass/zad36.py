print('Liczba podzielna przez 7, która przy dzieleniu przez 2, 3, 4, 5, 6 daje resztę 1 to: ')
x = 0
while True:
    if x % 7 == 0 and x % 2 == 1 and x % 3 == 1 and x % 4 == 1 and x % 5 == 1 and x % 6 == 1:
        print(x)
    if x == 10000:
        break
    else:
        x += 1
        continue