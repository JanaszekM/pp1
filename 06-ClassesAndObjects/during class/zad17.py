from math import gcd
class x():
    def __init__(self,lic,mian):
        self.lic = lic
        self.mian = mian
        
        
    def show(self):
        
        print(self.lic, '/', self.mian)
      
    def uprosc(self):
        print(int((self.lic/gcd(self.lic,self.mian))),'/',int((self.mian/gcd(self.lic,self.mian))))
        
b=x(10,25)
b.show()
b.uprosc()
        
        