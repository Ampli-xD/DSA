from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button

class AnchorLayoutExp(AnchorLayout):
    pass
class BoxLayoutExp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b=Button(text="HelloWorld", size_hint= (.5, .5))
        self.add_widget(b)
class MainWidget(Widget):
    pass
class TheLabApp(App):
    pass

TheLabApp().run()
