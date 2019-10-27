pesel = int(input('Podaj PESEL:'))
pesel = str(pesel)

rok = int(pesel[0:2])
gender = int(pesel[-2])
wiek = 2019-rok-1900
if gender==1 or gender==3 or gender==5 or gender==7 or gender==9:
    plec = 'Mężczyzna'
else:
    plec = 'Kobieta'

print(f"Wiek: {wiek}")
print(f"Płeć: {plec}")
