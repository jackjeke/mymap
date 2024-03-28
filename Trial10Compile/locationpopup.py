from kivymd.uix.dialog import MDDialog



class LocationPopUp(MDDialog):
    def __init__(self,data):
        super(). __init__()
        self.name=str(data[1])
        self.y=str(data[4])
        self.x=str(data[5])
        self.title="Reference Marks"
        
        self.text='Name:{}\nY:{}\nX:{}'.format(self.name,self.y,self.x)

        
     
