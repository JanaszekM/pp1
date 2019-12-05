class telewizor():
    def __init__(self):
        self.is_on= False
        self.channel_no = '1'
        self.channels=['TVP1','TVP2','Polsat','TVN','Filmbox']
    def on(self):
        self.is_on = True
    def off(self):
        self.is_on = False
        
    def set_channel(self,new_channel):
        
        self.channel_no = new_channel        
    def show_status(self):
        
        if self.is_on == True:
            print(f'zalaczony,{self.channel_no}')
        else:
            print('nie zalaczony')
            
    def set_channels(self):
        print(self.channels)
        
        
        
k=telewizor()

k.on()
k.set_channel(2)
k.show_status()
k.set_channels()