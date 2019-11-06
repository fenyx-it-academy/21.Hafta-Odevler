print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")

import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window
import comicwidgets
import toolbox
import generaloptions
import drawingspace
import statusbar
import style
Window.clearcolor = (100/255, 92/255, 2/255, 1/255)

Builder.load_file('toolbox.kv')                             # kv uzantili dosyalari import ediyoruz
Builder.load_file('drawingspace.kv')
Builder.load_file('generaloptions.kv')
Builder.load_file('comiccreator.kv')
Builder.load_file('statusbar.kv')
Builder.load_file('comicwidgets.kv')
Builder.load_file('style.kv')


class ComicCreator(AnchorLayout):
    pass


class ComicCreatorApp(App):
    def build(self):
        return ComicCreator()


if __name__ == "__main__":
    ComicCreatorApp().run()
