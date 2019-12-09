class student():
    licznik=100000;
    uczelnia='UEK';
    def __init__(self,imie,nazwisko,kier):
        self.imie=imie
        self.nazwisko=nazwisko
        self.kier=kier
        self.album=student.licznik
        student.licznik+=1
        
        
    def __str__(self):
        return self.imie + self.nazwisko + self.kier + str(self.album)+ ' '  + student.uczelnia 
    
x=student('M ','J ','IDK ')
y=student('A ','J ','IDK ')
z=student('D ','J ','IDK ')
print(x)
print(y)
print(z)
        
