print('Podaj login')
login=str(input())
print('Podaj haslo')
pwd=str(input())
if login=="marek" and pwd=="m-123":
    print('Podane dane są prawidłowe')
if login!="marek" or pwd!="m-123":
    print('Podane dane są nieprawidłowe')