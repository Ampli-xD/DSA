from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.network.urlrequest import UrlRequest


class AnchorLayoutExp(AnchorLayout):
    pass
class BoxLayoutExp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b=Button(text="HelloWorld", size_hint= (.5, .5), on_release=self.requests)
        self.add_widget(b)
    def got_json(self, req, result):
        print(result)            
    def failed(self):
        print("fail")
    def requests(self, *args):
        req = UrlRequest("https://syllabusx-web-server.onrender.com/secondsemesters/CSE", on_success=self.got_json, on_failure=self.failed)
class MainWidget(Widget):
    pass
class TheLabApp(App):
    pass

TheLabApp().run()
