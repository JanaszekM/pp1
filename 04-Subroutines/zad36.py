tab = [7, 5, [3, 6, [2]], 7, [1, [2, 3, [4]], 9, 2], 4]

tab=str(tab)
nt=[]
def myluv(tab):
    while '[' in tab:
        tab=tab.replace('[','')
        tab=tab.replace(']','')
        tab=tab.split(',')
        
    for i in tab:
        i=int(i)
        nt.append(i)
        
    print(sum(nt))
myluv(tab)
isinstance(tab)