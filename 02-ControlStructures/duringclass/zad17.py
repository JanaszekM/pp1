# y to liczny parzyste
# x to liczby nieparzyste
sumay=0
sumax=0
for y in range(1,51):
    if y%2==0:
        sumay+=y
print(f'suma liczb parzystych wynosi {sumay}.')
for x in range(0,51):
    if x%2!=0:
        sumax+=x
print(f'suma liczb nieparzystych wynosi {sumax}.')
    
    