class tl():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = ''
        self.channels_list=''
        self.vol = 0
        
    def volup(self):
        self.vol=self.vol+1
        if self.vol>10:
            self.vol=10
            return('Głośność 10')
        else:
            return(f'Głośność {self.vol}')
    def voldown(self):
        self.vol=self.vol-1
        if self.vol<0:
            self.vol=0
            return('Głośność 0')
        else:
            return(f'Głośność {self.vol}')
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
            if self.channel_no>len(self.channels):
                print(f'Telewizor jest załączony. Kanał {self.channel_no}.')
                print(f'Głośność: {self.vol}')
            else:
                print(f'Telewizor jest załączony. Kanał {self.channel_no} czyli {self.channels[(self.channel_no)-1]}')
                print(f'Istnieja taki kannaly :',self.channels)
                print(f'Głośność: {self.vol}')
        else:
            print('Telewizor nie jest załączony')
            print(self.vol)
            
b=tl()
b.on()
b.set_channel(9)
b.show_channels()
b.set_channels(['TVP1', 'TVP2', 'Polsat', 'TVN', 'Filmbox', 'HBO', 'LOGO TV', 'NETFLIX'])
b.show_channels()

b.volup()
b.voldown()
b.voldown()
b.show_status()