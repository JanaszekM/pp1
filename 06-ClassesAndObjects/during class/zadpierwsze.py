class University():    
    # konstruktor obiektu (metoda __init__)
    
    def __init__(self):
        # cechy obiektu (pola)
        self.name = 'UEK'    
    def set_name(self, new_name):
        self.name = new_name
        print(new_name)
    # zachowania obiektu (metody)
    def print_name(self):  
        print(self.name)

k=University()
#k.print_name()
k.set_name('ugh')

