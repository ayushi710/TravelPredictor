from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.graphics import *
from kivy.uix.button import Button
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder
from kivy.uix.dropdown import DropDown
from kivy.uix.popup import *
from kivy.base import runTouchApp
from Reverse_Convertor import *
from converter import *
import xlsxwriter
import pandas as pd
import numpy as np
import time

button_gender = Button(text='--Select--')
button_rv1 = Button(text='--Select--')
button_rv2 = Button(text='--Select--')
button_foreign = Button(text='--Select--')
button_purpose = Button(text='--Select--')
button_eating = Button(text='--Select--')
button_partner = Button(text='--Select--')
button_stay = Button(text='--Select--')
button_travel_taste = Button(text='--Select--')

class MyApp(App):

    def build(self):
        layout= GridLayout(cols=5)
        
        self.label1 = Label(text="Age")
        layout.add_widget(self.label1)
        self.age_taste = TextInput(text='', multiline=False)
        layout.add_widget(self.age_taste)

        self.label = Label(text="")
        layout.add_widget(self.label)

        self.label2 = Label(text="Gender")
        layout.add_widget(self.label2)
        dropdown_gender = DropDown()
        btn_male = Button(text='Male', size_hint_y=None, height=30)
        btn_male.bind(on_release=lambda btn: dropdown_gender.select(btn_male.text))
        dropdown_gender.add_widget(btn_male)
        btn_female = Button(text='Female', size_hint_y=None, height=30)
        btn_female.bind(on_release=lambda btn: dropdown_gender.select(btn_female.text))
        dropdown_gender.add_widget(btn_female)
        button_gender.bind(on_release=dropdown_gender.open) 
        dropdown_gender.bind(on_select=lambda instance, x: setattr(button_gender, 'text', x))
        layout.add_widget(button_gender)

        self.label3 = Label(text="Income")
        layout.add_widget(self.label3)
        self.income_taste = TextInput(text='', multiline=False)
        layout.add_widget(self.income_taste)

        self.label = Label(text="")
        layout.add_widget(self.label)

        self.label4 = Label(text="Budget")
        layout.add_widget(self.label4)
        self.budget_taste = TextInput(text='', multiline=False)
        layout.add_widget(self.budget_taste)

        self.label5 = Label(text="Recent Visit")
        layout.add_widget(self.label5)
        dropdown_rv1 = DropDown()
        btn_plain_rv1 = Button(text='Plain', size_hint_y=None, height=30)
        btn_plain_rv1.bind(on_release=lambda btn: dropdown_rv1.select(btn_plain_rv1.text))
        dropdown_rv1.add_widget(btn_plain_rv1)
        btn_beach_rv1 = Button(text='Beach', size_hint_y=None, height=30)
        btn_beach_rv1.bind(on_release=lambda btn: dropdown_rv1.select(btn_beach_rv1.text))
        dropdown_rv1.add_widget(btn_beach_rv1)
        btn_desert_rv1 = Button(text='Desert', size_hint_y=None, height=30)
        btn_desert_rv1.bind(on_release=lambda btn: dropdown_rv1.select(btn_desert_rv1.text))
        dropdown_rv1.add_widget(btn_desert_rv1)
        btn_hill_rv1 = Button(text='Hill', size_hint_y=None, height=30)
        btn_hill_rv1.bind(on_release=lambda btn: dropdown_rv1.select(btn_hill_rv1.text))
        dropdown_rv1.add_widget(btn_hill_rv1)
        button_rv1.bind(on_release=dropdown_rv1.open)
        dropdown_rv1.bind(on_select=lambda instance, x: setattr(button_rv1, 'text', x))
        layout.add_widget(button_rv1)

        self.label = Label(text="")
        layout.add_widget(self.label)

        self.label6 = Label(text="Recent Visit")
        layout.add_widget(self.label6)
        dropdown_rv2 = DropDown()
        btn_plain_rv2 = Button(text='Plain', size_hint_y=None, height=30)
        btn_plain_rv2.bind(on_release=lambda btn: dropdown_rv2.select(btn_plain_rv2.text))
        dropdown_rv2.add_widget(btn_plain_rv2)
        btn_beach_rv2 = Button(text='Beach', size_hint_y=None, height=30)
        btn_beach_rv2.bind(on_release=lambda btn: dropdown_rv2.select(btn_beach_rv2.text))
        dropdown_rv2.add_widget(btn_beach_rv2)
        btn_desert_rv2 = Button(text='Desert', size_hint_y=None, height=30)
        btn_desert_rv2.bind(on_release=lambda btn: dropdown_rv2.select(btn_desert_rv2.text))
        dropdown_rv2.add_widget(btn_desert_rv2)
        btn_hill_rv2 = Button(text='Hill', size_hint_y=None, height=30)
        btn_hill_rv2.bind(on_release=lambda btn: dropdown_rv2.select(btn_hill_rv2.text))
        dropdown_rv2.add_widget(btn_hill_rv2)
        button_rv2.bind(on_release=dropdown_rv2.open)
        dropdown_rv2.bind(on_select=lambda instance, x: setattr(button_rv2, 'text', x))
        layout.add_widget(button_rv2)

        self.label7 = Label(text="Foreign")
        layout.add_widget(self.label7)
        dropdown_foreign = DropDown()
        btn_yes = Button(text='Yes', size_hint_y=None, height=30)
        btn_yes.bind(on_release=lambda btn: dropdown_foreign.select(btn_yes.text))
        dropdown_foreign.add_widget(btn_yes)
        btn_no = Button(text='No', size_hint_y=None, height=30)
        btn_no.bind(on_release=lambda btn: dropdown_foreign.select(btn_no.text))
        dropdown_foreign.add_widget(btn_no)
        button_foreign.bind(on_release=dropdown_foreign.open)
        dropdown_foreign.bind(on_select=lambda instance, x: setattr(button_foreign, 'text', x))
        layout.add_widget(button_foreign)

        self.label = Label(text="")
        layout.add_widget(self.label)

        self.label8 = Label(text="Purpose")
        layout.add_widget(self.label8)
        dropdown_purpose = DropDown()
        btn_edu = Button(text='Education', size_hint_y=None, height=30)
        btn_edu.bind(on_release=lambda btn: dropdown_purpose.select(btn_edu.text))
        dropdown_purpose.add_widget(btn_edu)
        btn_work = Button(text='Work', size_hint_y=None, height=30)
        btn_work.bind(on_release=lambda btn: dropdown_purpose.select(btn_work.text))
        dropdown_purpose.add_widget(btn_work)
        btn_recreation = Button(text='Recreation', size_hint_y=None, height=30)
        btn_recreation.bind(on_release=lambda btn: dropdown_purpose.select(btn_recreation.text))
        dropdown_purpose.add_widget(btn_recreation)
        button_purpose.bind(on_release=dropdown_purpose.open)
        dropdown_purpose.bind(on_select=lambda instance, x: setattr(button_purpose, 'text', x))
        layout.add_widget(button_purpose)

        self.label9 = Label(text="Eating Habit")
        layout.add_widget(self.label9)
        dropdown_eating = DropDown()
        btn_veg = Button(text='Vegetarian', size_hint_y=None, height=30)
        btn_veg.bind(on_release=lambda btn: dropdown_eating.select(btn_veg.text))
        dropdown_eating.add_widget(btn_veg)
        btn_nveg = Button(text='Non-Vegetarian', size_hint_y=None, height=30)
        btn_nveg.bind(on_release=lambda btn: dropdown_eating.select(btn_nveg.text))
        dropdown_eating.add_widget(btn_nveg)
        button_eating.bind(on_release=dropdown_eating.open)
        dropdown_eating.bind(on_select=lambda instance, x: setattr(button_eating, 'text', x))
        layout.add_widget(button_eating)

        self.label = Label(text="")
        layout.add_widget(self.label)

        self.label12 = Label(text="Stay")
        layout.add_widget(self.label12)
        dropdown_stay = DropDown()
        btn_dormitory = Button(text='Dormitory', size_hint_y=None, height=30)
        btn_dormitory.bind(on_release=lambda btn: dropdown_stay.select(btn_dormitory.text))
        dropdown_stay.add_widget(btn_dormitory)
        btn_hostel = Button(text='Hostel', size_hint_y=None, height=30)
        btn_hostel.bind(on_release=lambda btn: dropdown_stay.select(btn_hostel.text))
        dropdown_stay.add_widget(btn_hostel)
        btn_hotel3 = Button(text='Hotel 3*', size_hint_y=None, height=30)
        btn_hotel3.bind(on_release=lambda btn: dropdown_stay.select(btn_hotel3.text))
        dropdown_stay.add_widget(btn_hotel3)
        btn_hotel4 = Button(text='Hotel 4*', size_hint_y=None, height=30)
        btn_hotel4.bind(on_release=lambda btn: dropdown_stay.select(btn_hotel4.text))
        dropdown_stay.add_widget(btn_hotel4)
        btn_hotel5 = Button(text='Hotel 5*', size_hint_y=None, height=30)
        btn_hotel5.bind(on_release=lambda btn: dropdown_stay.select(btn_hotel5.text))
        dropdown_stay.add_widget(btn_hotel5)
        button_stay.bind(on_release=dropdown_stay.open)
        dropdown_stay.bind(on_select=lambda instance, x: setattr(button_stay, 'text', x))
        layout.add_widget(button_stay)

        self.label10 = Label(text="Travel Taste")
        layout.add_widget(self.label10)
        dropdown_travel_taste = DropDown()
        btn_plain_travel_taste = Button(text='Plain', size_hint_y=None, height=30)
        btn_plain_travel_taste.bind(on_release=lambda btn: dropdown_travel_taste.select(btn_plain_travel_taste.text))
        dropdown_travel_taste.add_widget(btn_plain_travel_taste)
        btn_beach_travel_taste = Button(text='Beach', size_hint_y=None, height=30)
        btn_beach_travel_taste.bind(on_release=lambda btn: dropdown_travel_taste.select(btn_beach_travel_taste.text))
        dropdown_travel_taste.add_widget(btn_beach_travel_taste)
        btn_desert_travel_taste = Button(text='Desert', size_hint_y=None, height=30)
        btn_desert_travel_taste.bind(on_release=lambda btn: dropdown_travel_taste.select(btn_desert_travel_taste.text))
        dropdown_travel_taste.add_widget(btn_desert_travel_taste)
        btn_hill_travel_taste = Button(text='Hill', size_hint_y=None, height=30)
        btn_hill_travel_taste.bind(on_release=lambda btn: dropdown_travel_taste.select(btn_hill_travel_taste.text))
        dropdown_travel_taste.add_widget(btn_hill_travel_taste)
        button_travel_taste.bind(on_release=dropdown_travel_taste.open)
        dropdown_travel_taste.bind(on_select=lambda instance, x: setattr(button_travel_taste, 'text', x))
        layout.add_widget(button_travel_taste)

        self.label = Label(text="")
        layout.add_widget(self.label)

        self.label11 = Label(text="Preferred Partner")
        layout.add_widget(self.label11)
        dropdown_partner = DropDown()
        btn_family = Button(text='Family', size_hint_y=None, height=30)
        btn_family.bind(on_release=lambda btn: dropdown_partner.select(btn_family.text))
        dropdown_partner.add_widget(btn_family)
        btn_friends = Button(text='Friends', size_hint_y=None, height=30)
        btn_friends.bind(on_release=lambda btn: dropdown_partner.select(btn_friends.text))
        dropdown_partner.add_widget(btn_friends)
        btn_solo = Button(text='Solo', size_hint_y=None, height=30)
        btn_solo.bind(on_release=lambda btn: dropdown_partner.select(btn_solo.text))
        dropdown_partner.add_widget(btn_solo)
        button_partner.bind(on_release=dropdown_partner.open)
        dropdown_partner.bind(on_select=lambda instance, x: setattr(button_partner, 'text', x))
        layout.add_widget(button_partner)

        self.label = Label(text="")
        layout.add_widget(self.label)
        self.label = Label(text="")
        layout.add_widget(self.label)

        btn_submit = Button(text="Submit Details")
        btn_submit.background_normal=""
        btn_submit.background_color=[0,1,0,0.5]
        btn_submit.bind(on_press=self.buttonClicked_submit)
        layout.add_widget(btn_submit)

        return layout

    def updateExcel(self):
        a = int(self.age_taste.text)
        g = button_gender.text
        i = int(self.income_taste.text)
        b = int(self.budget_taste.text)
        t = button_travel_taste.text
        r1 = button_rv1.text
        r2 = button_rv2.text
        f = button_foreign.text
        p = button_purpose.text
        eat = button_eating.text
        st = button_stay.text
        partner = button_partner.text
        now_time = time.ctime()
        input_file = 'Travel.xlsx'
        sheet = 'Form Responses 1'
        df = pd.read_excel(input_file, sheet, header=0)
        features = list(df.columns[:13])
        new_df = pd.DataFrame([[now_time,a, g, i, b, t, r1, r2, f, p, eat, st, partner]], columns=features)
        df = df.append(new_df, ignore_index=True)
        writer = pd.ExcelWriter(input_file, engine='xlsxwriter')
        df.to_excel(writer, sheet, index=False)
        writer.save()

    def buttonClicked_submit(self,btn):
        a = int(self.age_taste.text)
        g = int(gender_converter(button_gender.text))
        i = int(self.income_taste.text)
        b = int(self.budget_taste.text)
        t = int(TravelTaste_converter(button_travel_taste.text))
        r1 = int(RecentVisit1_converter(button_rv1.text))
        r2 = int(RecentVisit2_converter(button_rv2.text))
        f = int(foreign_converter(button_foreign.text))
        p = int(purpose_converter(button_purpose.text))
        eat = int(EatingHabit_converter(button_eating.text))
        st = int(Stay_converter(button_stay.text))
        partner = int(PrefferedPartner_converter(button_partner.text))
        input_file = 'new.xlsx'
        sheet = 'Sheet1'
        df = pd.read_excel(input_file, sheet, header=0)
        features = list(df.columns[:12])
        new_df = pd.DataFrame([[a, g, i , b, t, r1, r2, f, p, eat, st, partner]], columns=features)
        df = df.append(new_df, ignore_index=True)
        writer = pd.ExcelWriter(input_file, engine='xlsxwriter')
        df.to_excel(writer, sheet, index=False)
        writer.save()
        self.updateExcel()
        popup = Popup(title='Thank you!', content=Label(text='Your response has been successfully submitted'),
                      auto_dismiss=False, size=(200, 200))
        popup.open()


if __name__ == '__main__':
    MyApp().run()
