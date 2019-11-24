
try: 
    tab = []    
    while True: 
        tab.append(int(input('Podaj liczbę: '))) 
except: 
    print('stop')
    
def idk(tab):
    newtab=[]
    for i in tab:
        if i not in newtab:
            newtab.append(i)
    print(newtab)
idk(tab)

