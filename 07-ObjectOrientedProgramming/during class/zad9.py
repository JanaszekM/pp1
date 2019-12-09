class Message():
    def __init__(self):
        self.message = ''
    def set_message(self,message):
        return message[0].upper()
    
    
x=Message()
print(x.set_message('wedfs'))