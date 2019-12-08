class tl():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = ''
        self.channels_list=''
        
    def on(self):
        self.is_on = True
    
    def off(self):
        self.is_on = False
        
    def set_channel(self,new_channel_no):
        self.channel_no = new_channel_no
        
    def set_channels(self, channels_list):
        channels = []
        for x in channels_list:
            channels.append(x)
        self.channels = channels
    def show_channels(self):
        print('LISTA KANAŁÓW TV')
        if self.channels=='':
            print('Telewizor niezaprogramowany.')
        else:
            for n in range(0,len(self.channels)):
                j=int(n)
                print(n+1,self.channels[j])
            
    def show_status(self):
        if self.is_on == True:
            print(f'Telewizor jest załączony. Kanał {self.channel_no}')
            print(f'Istnieja taki kannaly :',self.channels)
        else:
            print('Telewizor nie jest załączony')
            
b=tl()
b.on()
b.set_channel(3)
b.show_channels()
b.set_channels(['TVP1', 'TVP2', 'Polsat', 'TVN', 'Filmbox'])
b.show_channels()
b.show_status()