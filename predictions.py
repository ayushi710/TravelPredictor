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

        btn_taste = Button(text="Travel Taste")
        btn_taste.bind(on_press=self.buttonClicked_taste)
        layout.add_widget(btn_taste)

        btn_budget = Button(text="Budget")
        btn_budget.bind(on_press=self.buttonClicked_budget)
        layout.add_widget(btn_budget)

        btn_stay = Button(text="Stay")
        btn_stay.bind(on_press=self.buttonClicked_stay)
        layout.add_widget(btn_stay)

        btn_age = Button(text="Age")
        btn_age.bind(on_press=self.buttonClicked_age)
        layout.add_widget(btn_age)

        btn_partner = Button(text="Partner")
        btn_partner.bind(on_press=self.buttonClicked_partner)
        layout.add_widget(btn_partner)

        btn_foreign = Button(text="Foreign")
        btn_foreign.bind(on_press=self.buttonClicked_foreign)
        layout.add_widget(btn_foreign)
               
        return layout

    def buttonClicked_taste(self,btn):
        os.system('python taste_predict.py')
    
    def buttonClicked_budget(self,btn):
        os.system('python budget_predict.py')

    def buttonClicked_stay(self,btn):
        os.system('python stay_predict.py')
    
    def buttonClicked_age(self,btn):
        os.system('python age_predict.py')

    def buttonClicked_partner(self,btn):
        os.system('python partner_predict.py')
    
    def buttonClicked_foreign(self,btn):
        os.system('python foreign_predict.py')

if __name__ == '__main__':
    MyApp().run()