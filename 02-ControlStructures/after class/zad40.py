import random
amount1 = 0
amount2 = 0
amount3 = 0
amount4 = 0
amount5 = 0
amount6 = 0

x = 0
while x < 100:
    x+=1
    wylosowany=random.randrange(1,7)
    if wylosowany==1:
        amount1+=1
    elif wylosowany==2:
        amount2+=1
    elif wylosowany==3:
        amount3+=1
    elif wylosowany==4:
        amount4+=1
    elif wylosowany==5:
        amount5+=1
    elif wylosowany==6:
        amount6+=1
print(f"Jedynka: {amount1}")
print(f"Dwójka: {amount2}")
print(f"Trójka: {amount3}")
print(f"Czwórka: {amount4}")
print(f"Piątka: {amount5}")
print(f"Szóstka: {amount6}")