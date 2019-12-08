class bk():
    def __init__(self,title,author,pages):
        self.isopen = False
        self.title = title
        self.author = author
        self.pages= pages
        self.current_page = 0
        
    def openbook(self):
        self.isopen = True
    
    def clsbook(self):
        self.isopen = False
        
    def nextpage(self):
        if self.isopen == True:
            self.current_page=self.current_page+1
            if self.current_page<0:
                self.current_page=0
                print('Początek')
            else:
                print(f'Str: {self.current_page}')
        else:
                print('Book closed')
    def prevpage(self):
        if self.isopen == True:
            self.current_page=self.current_page-1
            if self.current_page>self.pages:
                self.current_page=1024
                print('Koniec')
            else:
                print(f'Str: {self.current_page}')
        else:
                print('Book closed')
            
    def status(self):
        print(self.title)
        print(self.author)
        print(self.pages)
        print(self.current_page)
        
        
k=bk('Gone with the Wind','Margaret Mitchell',1024)
k.openbook()
k.status()
k.nextpage()
k.status()

k.nextpage()