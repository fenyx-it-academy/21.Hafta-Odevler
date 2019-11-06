from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout

class DrawingSpace(RelativeLayout):
    def on_children(self, instance, value):
        self.status_bar.counter = len(self.children)

class DrawingApp(App):
    def build(self):
        return DrawingSpace()


if __name__=="__main__":
    DrawingApp().run()