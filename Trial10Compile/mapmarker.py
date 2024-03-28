from kivy_garden.mapview import MapMarkerPopup
from locationpopup import LocationPopUp

class MapMarker(MapMarkerPopup):
    market_data=None
    source="marker2.png"
   
    def on_release(self):
        menu=LocationPopUp(self.market_data)
##        menu=LocationPopUp()
        menu.open()
##        menu.data=self.market_data
        
        
