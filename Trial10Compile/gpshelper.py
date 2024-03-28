from kivymd.app import MDApp
from gpsblinker import GpsBlinker
from kivy.utils import platform
from kivymd.uix.dialog import MDDialog

class GpsHelper():
    has_centered_map=False
    def run (self):
##        pass
        #starts blinking gPS blinker

        #get reference to GpsBlinker then call blink()

        gps_blinker=MDApp.get_running_app().root.ids.my_blinker
        gps_blinker.blink()
        #request permission from android
        if platform=='android':
            from android.permissions import Permission,request_permission
            def callback(permission,results):
                if all([res for res in results]):
                    print('Got all permissions')
                else:
                    print('Did not get all permissions')
            request_permissions([Permission.ACCESS_COARSE_LOCATION,Permission.ACCESS_FINE_LOCATION],callback)

        if platform=='android':
            from plyer import gps
            gps.configure(on_location=self.update_blinker_position,on_status=self.on_auth_status)
            gps.start(minTime=1000,minDistance=0)
    def update_blinker_position(self,*args,**kwargs):
        my_lat=kwargs['lat']
        my_lon=kargs['lon']
        gps_blinker=MDApp.get_running_app().root.ids.my_blinker
        gps_blinker.lat=my_lat
        gps_blinker.lon=my_lon
        #center map on gps
        if not self.has_centered_map:
            mapp=MDApp.get_running_app().root.ids.mapview
            mapp.center_on(my_lat,my_lon)
            self.has_centered_map=True
    def on_auth_status(self,general_status,status_message):
        if general_status=='provider_enabled':
            pass
        else:
            self.open_gps_access_popup()
    def open_gps_access_popup(self):
        dialog=MDDialog(title="GPS Error",text="You need to enable GPS")
        dialog.size_hint=(0.8,0.8)
        dialog.pos_hint={'center_x':0.5,'center_y':0.5}
        dialog.open()
