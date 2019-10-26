print('Podaj wzrost w cm')
wzrost = float(input())
print('Podaj wage w kg')
masa=float(input())
bmi=(masa) / ((wzrost/100)**2)
print(f'Wskaźnik BMI: {bmi:.1f}')
if bmi<18.5:
    print('Niedowaga')
elif 18.5<= bmi <= 24.9:
    print('Waga prawidłowa')
elif 25 <= bmi <= 29.9:
    print('Nadwaga')
elif bmi > 30:
    print('Otyłość')