
class music():
    
    def __init__(self,author, title, album, rok):
        self.author = author
        self.title = title
        self.album = album
        self.rok = rok
    
    def __str__(self):
        return f'''
Wykonawca: {self.author}
Utwór: {self.title}
Album: {self.album}
Rok: {self.rok}'''
        
    
x= music('f','f','d','e')
print(x)

