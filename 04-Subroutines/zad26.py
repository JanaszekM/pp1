
pod=int()

dochod=int(input('Podaj dochód: '))

def podatek(dochod):
    
    if dochod<=5000:
        pod=0.17
        wynik=dochod*0.17
    else:
        pod=0.32
        wynik=5000*0.17+(dochod-5000)*0.32
    print(f'Podatek należny: {wynik} zł')
    
podatek(dochod)