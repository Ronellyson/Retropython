import os
import subprocess as s
import sys
import RetroPython 
import webbrowser
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.graphics import Canvas
from Games import *

class System (App):
    
    def build(self):
        InterfacePrincipal = FloatLayout()
        

        Images = FloatLayout()
        ListadeGames = ScrollView()
        Games = FloatLayout()
        descriptions = FloatLayout()
        NomeMenu = FloatLayout()
        Background = FloatLayout()
        
        label1 = Label(text='Lista de Games:', font_size=30,pos_hint={'x':0.1, 'y':0.9},size_hint_x=0.28,size_hint_y=0.05)
        Background_Lista = wimg = Image(source='Retropython\B_L1.bmp', pos_hint={'x':-0.3, 'y':-0.005})
        Background_Lista2 = wimg = Image(source='Retropython\B_L2.bmp', pos_hint={'x':0, 'y':-0.005})
        
        label2 = Label(text='Descrição:', font_size=30,pos_hint={'x':0.23, 'y':0.9},size_hint_x=1,size_hint_y=-1)
        Background_descrição = wimg = Image(source='Retropython\B_D1.bmp', pos_hint={'x':0.23, 'y':-0.43})
        Background_descrição2 = wimg = Image(source='Retropython\B_D2.bmp', pos_hint={'x':0.485, 'y':-0.35},size_hint_y=0.95,size_hint_x=0.5)

        id = 1
        y= 0.8
        botoes = []
        description = Label(text=RetroPython.getURLDescription(id),text_size=(350,180), font_size=16,valign='top',halign='center',pos_hint={'x':0.5, 'y':0.02}, size_hint_x=0.48, size_hint_y=0.35)
        wimg = Image(source=RetroPython.getURLImage(id) , pos_hint={'x':0.245, 'y':0.235})
        def LinkButton2(button2):
            print(button2.id)
            wimg.source=RetroPython.getURLImage(button2.id)
            description.text=RetroPython.getURLDescription(button2.id)
        def LinkButton(button):
            button_source_windows=RetroPython.getURLISourceWin(button.id)
            button_source_linux=RetroPython.getURLISourceLinux(button.id)
            plataforma = sys.platform
            if 'win' in plataforma:
                os.startfile(button_source_windows)
            if 'linux' in plataforma:
                s.Popen(button_source_linux)
        for item in range(RetroPython.countItems()):
            
                

            button = Button(text=str(RetroPython.getURLName(id)),pos_hint={'x':0.01, 'y':y},size_hint_x=0.3435,size_hint_y=0.05,on_release=LinkButton,id=str(id))
            button2 = Button(text='Ver Sobre',pos_hint={'x':0.36, 'y':y},size_hint_x=0.1145,size_hint_y=0.05, on_release=LinkButton2,id=str(id))
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
        
        
        Background.add_widget(Background_Lista2)
        Background.add_widget(Background_descrição2)
        
        Background.add_widget(Background_descrição)
        Background.add_widget(Background_Lista)
        ListadeGames.add_widget(Games)

        InterfacePrincipal.add_widget(Background)
        InterfacePrincipal.add_widget(descriptions)
        InterfacePrincipal.add_widget(NomeMenu)
        InterfacePrincipal.add_widget(ListadeGames)
        InterfacePrincipal.add_widget(Images)
        
        return InterfacePrincipal
System().run()   