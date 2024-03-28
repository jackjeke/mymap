from kivymd.app import MDApp
from farmersmapview import FarmersMapView
from searchpopup import SearchPopup
import sqlite3
from gpsblinker import GpsBlinker
from gpshelper import GpsHelper
from kivy.core.window import Window
##Window.size=(360,600)



class MainApp(MDApp):
    conn=None
    curs=None
    finder=None

    def on_start(self):
        self.theme_cls.primary_palette='BlueGray'
        ##connect to database
        self.conn=sqlite3.connect('My_DBASE.db')
        self.curs=self.conn.cursor()

        #search popup menu

        self.finder=SearchPopup()
        
        
        
        

        #initiate GPS
##        GpsBlinker().blink()
##        app=MDApp.get_running_app()
##        wid=app.root.ids.my_blinker
##        wid.blink()
        GpsHelper().run()

       
    

        
        


MainApp().run()
