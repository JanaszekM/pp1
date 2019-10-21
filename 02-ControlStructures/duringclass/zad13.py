print('Podaj x')
x=int(input())
print('Podaj y')
y=int(input())
if x>0 and y>0:
    print(f'Punkt P({x},{y}) znajduje się w pierwszej ćwiartce')
if x<0 and y>0:
    print(f'Punkt P({x},{y}) znajduje się w drugiej ćwiartce')
if x<0 and y<0:
    print(f'Punkt P({x},{y}) znajduje się w trzeciej ćwiartce')


if x>0 and y<0:
    print(f'Punkt P({x},{y}) znajduje się w czwartej ćwiartce')
if x==0 :
    print(f'Punkt P({x},{y}) położony jest na osi X')
    
if y==0 :
    print(f'Punkt P({x},{y}) położony jest na osi Y')