##from kivymd.uix.dialog import MDInputDialog
from kivymd.uix.dialog import MDDialog
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.app import MDApp


##textinput = TextInput(text='Hello world')



class SearchPopup(MDDialog):
##    
    def __init__(self,**kwargs):
        super(). __init__(**kwargs)
##        
##        self.buttons=[search_button]
    
    

   
    
        bxlyout=BoxLayout(orientation='vertical')
        self.txt_inp=Label(text='Search By Name',color='black')
        self.txt_inp1=TextInput(text='',multiline=False,on_text_validate=self.get_address)
        search_button=MDFlatButton(text='Take Me There',on_release=self.get_address)
        
        bxlyout.add_widget(self.txt_inp)
        bxlyout.add_widget(self.txt_inp1)
##        bxlyout.add_widget(search_button)
        self.add_widget(bxlyout)
        self.size_hint=0.4,0.1

    def get_address(self,*args):
##        print('Hie')
        address=self.txt_inp1.text
        print(address)
        
