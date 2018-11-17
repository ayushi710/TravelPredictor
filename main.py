import os
import sys
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.graphics import *
from kivy.uix.button import Button
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder
from kivy.uix.dropdown import DropDown
from kivy.base import runTouchApp

class MyApp(App):

    def build(self):
        layout= GridLayout(cols=2)
        
        label= Label(text="Travel Predictor", font_size='40sp')
        layout.add_widget(label)

        label= Label()
        layout.add_widget(label)

        btn_data = Button(text="Data Entry")
        btn_data.bind(on_press=self.buttonClicked_data)
        layout.add_widget(btn_data)

        btn_predict = Button(text="Predict Results")
        btn_predict.bind(on_press=self.buttonClicked_predict)
        layout.add_widget(btn_predict)
               
        return layout

    def buttonClicked_data(self,btn):
        os.system('python data_entry.py')
    
    def buttonClicked_predict(self,btn):
        os.system('python predictions.py')

if __name__ == '__main__':
    MyApp().run()