from kivy_garden.mapview import MapView
from kivy.clock import Clock
from kivymd.app import MDApp
from mapmarker import MapMarker

class FarmersMapView(MapView):
    timer=None
    ids=[]


    def start_getting_markets_in_fov(self):

        try:
            self.timer.cancel()
        except Exception:
            pass
        self.timer=Clock.schedule_once(self.get_markets_in_fov,1)

    def get_markets_in_fov(self,*args):
        app=MDApp.get_running_app()
        curs=app.curs
        min_lat,min_lon,max_lat,max_lon=self.get_bbox()
        
        curs.execute("SELECT * FROM attributes WHERE LATITUDE>:min_lat AND LATITUDE<:max_lat AND LONGITUDE>:min_lon AND LONGITUDE<:max_lon",
                     {'min_lat':min_lat,'min_lon':min_lon,'max_lat':max_lat,'max_lon':max_lon})
        markets=curs.fetchall()

        for market in markets:
            idx=market[0]
            if idx in self.ids:
                pass
            else:
                self.add_market(market)
    def add_market(self,market):
        lat,lon=market[3],market[2]
        
        marker=MapMarker(lat=lat,lon=lon)
        marker.market_data=market
        self.add_widget(marker)

        ##monitor the added marker_popups
        idx=market[0]
        self.ids.append(idx)

        
        
        



    



