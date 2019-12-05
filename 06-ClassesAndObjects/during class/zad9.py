class University():    
    # konstruktor obiektu (metoda __init__)
    
    def __init__(self):
        # cechy obiektu (pola)
        self.name = 'UEK'
        self.fullname= 'Uniwersyty Ekonomiczny w Krakowie'
    def set_name(self, new_name):
        self.name = new_name
        print(new_name)
    # zachowania obiektu (metody)
    def print_name(self):  
        print(self.name)
    
    def print_fullname(self):
        print(self.fullname)
        
    def set_fullname(self, new_fullname):
        self.fullname = new_fullname
        print(new_fullname)

k=University()
#k.print_name()
#k.set_name('AGH')
k.print_fullname()
k.set_fullname('Uniwersytet Simowy')
