import re
global string
string=''



def idk(string):
    string=input('Podaj ciąg znaków')
    import re
    x=re.findall('[A-Z]', string)
    print(x)
    
idk(string)
    
    
