
jezyk=['Java','Python','JavaScript','C++','C#','Ruby','Perl','PHP','C','Android']
wartosci=['61','47','37','32','26','18','14','9','7']


def rysuj(jezyk,wartosci):
    p='#'
    i=0
    for x in wartosci:
        x=int(x)
        #for i in jezyk:
        print(f'{jezyk[i]}: {int(x/2)*p}')
        i+=1
        
rysuj(jezyk,wartosci)
    


