z= int(input('podaj liczbe: '))
tab=[1,2,3,4,5,6,7,8,9,10]
for x in tab:
    i=0
    while i != x:
        y=float(z/x)
        i += 1
    print(f"{z}/{x}= {y} ")