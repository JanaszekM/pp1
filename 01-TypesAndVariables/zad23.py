
print('Podaj wzrost:')
cm=float(input())
stopy=(cm//30.48)
x=cm%30.48
cale=(x/2.54)

print(f'Mam {cm} cm wzrostu, tj. {stopy} stóp i {cale:.0f} cali.')
