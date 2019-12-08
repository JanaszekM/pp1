class tl():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = 'Telewizor niezaprogramowany.'

    def on(self):
        self.is_on = True
    
    def off(self):
        self.is_on = False
        
    def show_status(self):
        if self.is_on == True:
            print(f'Telewizor jest załączony. Kanał {self.channel_no}')
        else:
            print('Telewizor nie jest załączony')
            
b=tl()
b.on()
b.show_status()