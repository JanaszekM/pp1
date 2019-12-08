class tl():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = 'Telewizor niezaprogramowany.'

    def on(self):
        self.is_on = True
    
    def off(self):
        self.is_on = False
        
    def set_channel(self,new_channel_no):
        self.channel_no = new_channel_no 
        
    def show_status(self):
        if self.is_on == True:
            print(f'Telewizor jest załączony. Kanał {self.channel_no}')
        else:
            print('Telewizor nie jest załączony')
            
b=tl()
b.on()
b.set_channel(3)
b.show_status()