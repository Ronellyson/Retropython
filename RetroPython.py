from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
import gamelist

class Imagem (App):
    def build(self):
        wimg = Image(source=gamelist.getURLImage(), pos_hint={'x':0.23, 'y':0.23})
        return wimg
Imagem().run()        