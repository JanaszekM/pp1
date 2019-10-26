x=int(input('Podaj limit prędkości: '))
speed=int(input('Podaj prędkość: '))
overspeed=speed-x
fine=''
if overspeed<=10:
    fine=overspeed*5
    print(f'Mandat (zł):{fine} ')
else:
    fine=50+(overspeed-10)*15
    print(f'Mandat (zł):{fine} ')