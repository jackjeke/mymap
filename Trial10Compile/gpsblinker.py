from kivy_garden.mapview import MapMarker
from kivymd.app import MDApp
from kivy.animation import Animation

class GpsBlinker(MapMarker):
    
    
    
##    def __init__(self,**kwargs):
##        super(). __init__(**kwargs)
    def blink(self):
    
        
        
        anim=Animation(opacity=0,blink_size=50)
##        anim=Animation(opacity=0)
       #when the animation completes,reset the animation to repeat
        anim.bind(on_complete=self.reset)
        anim.start(self)
##        print('SZ1=',self.blink_size)
        

    def reset(self,*args):

        self.opacity=1
        self.blink_size=self.default_blink_size
##        print('SZ2=',self.default_blink_size)
        self.blink()
##        self.__init__()

