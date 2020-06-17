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
        Games = FloatLayout()
        
        label1 = Label(text='Lista de Games:', font_size=30,pos_hint={'x':0.1, 'y':0.9},size_hint_x=0.28,size_hint_y=0.05)
        label2 = Label(text='Descrição:', font_size=30,pos_hint={'x':0.23, 'y':0.9},size_hint_x=1,size_hint_y=-1)

        # print(gamelist.countItems())
        id = 1
        y= 0.8
        botoes = []
        for item in range(gamelist.countItems()):
           button = Button(text=str(gamelist.getURLName(id)),pos_hint={'x':0.01, 'y':y},size_hint_x=0.458,size_hint_y=0.05)
           Games.add_widget(button)
           id = id+1
           y = y - 0.1
        id =1
           
        wimg = Image(source=gamelist.getURLImage(), pos_hint={'x':0.23, 'y':0.23})
        Games.add_widget(label1)
        Games.add_widget(label2)
        Games.add_widget(wimg)
        
        return Games 
Imagem().run()        