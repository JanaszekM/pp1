
class University():
    
    def __init__(self, name):
        self.name = name 
    
    def __str__(self):
        return self.name + " is a whole circus."
    
my_university = University('UEK Kraków')
print(my_university)      



