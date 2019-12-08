class konto():
    def __init__(self, nr):
        self.rachunek = str(nr)
        self.saldo = 0
        
    def wplata(self,ilosc):
        self.saldo=+ilosc
        
    def wyplata(self,ilosc):
        if self.saldo < ilosc:
            print('Niewystarczająca ilość środków na rachunku')
        else:
            self.saldo=-ilosc
        
    def status(self):
        if len(self.rachunek) == 26:
            print(self.rachunek[0:2] + " " + self.rachunek[2:6] + " " + self.rachunek[6:10] + " " + self.rachunek[10:14] + " " + self.rachunek[14:18] + " " + self.rachunek[18:22] + " " + self.rachunek[22:26])
            print(f'Saldo: {self.saldo} zl')
            
b=konto(12345678901234567890123456)
b.status()
b.wplata(25.30)
b.status()
