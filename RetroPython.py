from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
from kivy.core.window import Window
from Games import *
import gamelist 
import os
import subprocess as s

#forçar framebuster
# Config.set('graphics','widht','640')
# Config.set('graphics','height','480')


class Retropython (App):
    
    def build(self):
        InterfacePrincipal = FloatLayout()
        

        Images = FloatLayout()
        ListadeGames = ScrollView()
        Games = FloatLayout()
        descriptions = FloatLayout()
        NomeMenu = FloatLayout()
        
        label1 = Label(text='Lista de Games:', font_size=30,pos_hint={'x':0.1, 'y':0.9},size_hint_x=0.28,size_hint_y=0.05)
        label2 = Label(text='Descrição:', font_size=30,pos_hint={'x':0.23, 'y':0.9},size_hint_x=1,size_hint_y=-1)
        
        

        id = 1
        y= 0.8
        botoes = []
        description = Label(text=gamelist.getURLDescription(id),text_size=(350,180), font_size=16,valign='top',halign='center',pos_hint={'x':0.5, 'y':0.02}, size_hint_x=0.48, size_hint_y=0.35)
        wimg = Image(source=gamelist.getURLImage(id) , pos_hint={'x':0.23, 'y':0.23})
        def LinkButton2(button2):
            print(button2.id)
            wimg.source=gamelist.getURLImage(button2.id)
            description.text=gamelist.getURLDescription(button2.id)
        def LinkButton(button):
            button_source=gamelist.getURLISource(button.id)
            # s.Popen(button_source)
            os.startfile(button_source)
            
        for item in range(gamelist.countItems()):
            
                

            button = Button(text=str(gamelist.getURLName(id)),pos_hint={'x':0.01, 'y':y},size_hint_x=0.3435,size_hint_y=0.05,on_press=LinkButton,id=str(id))
            button2 = Button(text='Ver Sobre',pos_hint={'x':0.36, 'y':y},size_hint_x=0.1145,size_hint_y=0.05, on_press=LinkButton2,id=str(id))
            Games.add_widget(button)
            Games.add_widget(button2)
            id = id+1
            y = y - 0.1
        id =1

        # wimg = Image(source='', pos_hint={'x':0.23, 'y':0.23})
        
        NomeMenu.add_widget(label1)
        NomeMenu.add_widget(label2)

        Images.add_widget(wimg)

        descriptions.add_widget(description)

        ListadeGames.add_widget(Games)


        InterfacePrincipal.add_widget(descriptions)
        InterfacePrincipal.add_widget(NomeMenu)
        InterfacePrincipal.add_widget(ListadeGames)
        InterfacePrincipal.add_widget(Images)
        
        return InterfacePrincipal
Retropython().run()   