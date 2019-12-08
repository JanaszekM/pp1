class tl():
    def __init__(self):
        self.is_on = False
        self.channel = 1
        self.channels = 'Telewizor niezaprogramowany.'

    def on(self):
        self.is_on = True
    
    def off(self):
        self.is_on = False
        
    def show_status(self):
        if self.is_on == True:
            print('Telewizor jest załączony')
        else:
            print('Telewizor nie jest załączony')
            
b=tl()
b.on()
b.show_status()