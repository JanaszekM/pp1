from statistics import median
import re
tab=[2, 3, 5, 2, 9, 8, 1, 3, 9, 1, 1, 4, 7, 7, 1, 4]
#cotojest='2, 3, 5, 2, 9, 8, 1, 3, 9, 1, 1, 4, 7, 7, 1, 4'
srodkowa=''
liczby='1','2','3','4','5','6','7','8','9'
cotojest=str(tab)
def idk():
    x=sorted(tab)
    b=int(0)
    mediana= median(x)
    print(f'Mediana wynosi: {mediana}.')
    #print(x)
    domin=[]
    for i in liczby:
        domin=re.findall(i,cotojest)
        
        if len(domin)>b:
            b=len(domin)
            print(f'Dominantą jest liczba: {i}: pojawia się {b} razy.')
    
idk()