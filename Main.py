from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.animation import Animation


class AL(AnchorLayout):
    def animate_it(self, widget, *arg):
        animate = Animation(
            background_color= (0,0,1,1)
        )

class MainKv(App):
    Window.size=(50, 80)
    pass



MainKv().run()