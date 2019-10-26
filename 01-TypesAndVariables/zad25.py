print(f'Podaj nr rachunku bankowego:')
nr=str(input())
if len(nr)== 26:
    print(nr[0:2],nr[2:6],nr[6:10], nr[10:14],nr[14:18],nr[18:22],nr[22:26])
elif len(nr)>26:
    print('Numer za długi')
elif len(nr)<26:
    print('Numer za krótki')