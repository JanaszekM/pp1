import random
print('Podaj, ile oczek kostki wyrzucił komputer:')
x=int(input())
print('Komputer wyrzucił:')
y=random.randrange(1,7)
print(y)
if x==y:
    print('Zgadłeś: True')
else:
    print('Zgadłeś: False')
