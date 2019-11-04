liczba = int(input('Liczba:'))
tablica = [15,38,7,23,14]
i=0

def wystepuje(liczba, tablica):
    status=0
    for i in tablica:
        if liczba==i:
            status=1
    if status==1:
        print('Wystepuje')
    else:
        print('nie wystepuje')
wystepuje(liczba,tablica)

    
    
    

