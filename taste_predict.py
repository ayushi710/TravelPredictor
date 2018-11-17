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
import pandas as pd
import numpy as np
from patsy.highlevel import dmatrices
from sklearn.linear_model import LogisticRegression
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from converter import *
from Reverse_Convertor import *
import smtplib


button_gender = Button(text="--Select--")
button_rv1 = Button(text='--Select--')
button_rv2 = Button(text='--Select--')
button_foreign = Button(text='--Select--')
button_purpose = Button(text='--Select--')
button_eating = Button(text='--Select--')
button_stay = Button(text='--Select--')
button_partner = Button(text='--Select--')

def taste():
    input_file = 'new.xlsx'
    sheet = 'Sheet1'
    df = pd.read_excel(input_file, sheet, header=0)
    y, X = dmatrices('TravelTaste ~ Age + Gender +Income+ TravelBudget+RecentVisit1+RecentVisit2+ Foreign+ EatingHabit +\
                       Stay+ Purpose + PreferredPartner ', df, return_type='dataframe')
    y = np.ravel(y)
    return y, X

class MyApp(App):

    def build(self):
        layout= GridLayout(cols=4)
        
        self.label1 = Label(text="Age")
        layout.add_widget(self.label1)
        self.age_taste = TextInput(text='', multiline=False)
        layout.add_widget(self.age_taste)

        self.label2 = Label(text="Gender")
        layout.add_widget(self.label2)
        dropdown_gender = DropDown()
        btn_male = Button(text='Male', size_hint_y=None, height=30)
        btn_male.bind(on_release=lambda btn: dropdown_gender.select(btn_male.text))
        dropdown_gender.add_widget(btn_male)
        btn_female = Button(text='Female', size_hint_y=None, height=30)
        btn_female.bind(on_release=lambda btn: dropdown_gender.select(btn_female.text))
        dropdown_gender.add_widget(btn_female)
        #global button_gender = Button(text='--Select--')
        button_gender.bind(on_release=dropdown_gender.open)
        dropdown_gender.bind(on_select=lambda instance, x: setattr(button_gender, 'text', x))
        layout.add_widget(button_gender)

        self.label3 = Label(text="Income")
        layout.add_widget(self.label3)
        self.income_taste = TextInput(text='', multiline=False)
        layout.add_widget(self.income_taste)

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
        #button_foreign = Button(text='--Select--')
        button_foreign.bind(on_release=dropdown_foreign.open)
        dropdown_foreign.bind(on_select=lambda instance, x: setattr(button_foreign, 'text', x))
        layout.add_widget(button_foreign)

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
        #button_purpose = Button(text='--Select--')
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
        #button_eating = Button(text='--Select--')
        button_eating.bind(on_release=dropdown_eating.open)
        dropdown_eating.bind(on_select=lambda instance, x: setattr(button_eating, 'text', x))
        layout.add_widget(button_eating)

        self.label10 = Label(text="Stay")
        layout.add_widget(self.label10)
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
        #button_stay = Button(text='--Select--')
        button_stay.bind(on_release=dropdown_stay.open)
        dropdown_stay.bind(on_select=lambda instance, x: setattr(button_stay, 'text', x))
        layout.add_widget(button_stay)

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
        #button_partner = Button(text='--Select--')
        button_partner.bind(on_release=dropdown_partner.open)
        dropdown_partner.bind(on_select=lambda instance, x: setattr(button_partner, 'text', x))
        layout.add_widget(button_partner)

        self.label12 = Label(text="Email")
        layout.add_widget(self.label12)
        self.email = TextInput(text='', multiline=False)
        layout.add_widget(self.email)

        btn_lr = Button(text="Logical Regression")
        btn_lr.bind(on_press=self.buttonClicked_LR)
        layout.add_widget(btn_lr)
        self.lr_taste = TextInput(text='', multiline=False)
        layout.add_widget(self.lr_taste)

        btn_dt = Button(text="Decision Tree")
        btn_dt.bind(on_press=self.buttonClicked_DT)
        layout.add_widget(btn_dt)
        self.dt_taste = TextInput(text='', multiline=False)
        layout.add_widget(self.dt_taste)

        btn_svm = Button(text="SVM")
        btn_svm.bind(on_press=self.buttonClicked_SVM)
        layout.add_widget(btn_svm)
        self.svm_taste = TextInput(text='', multiline=False)
        layout.add_widget(self.svm_taste)

        btn_rf = Button(text="Random Forest")
        btn_rf.bind(on_press=self.buttonClicked_RF)
        layout.add_widget(btn_rf)
        self.rf_taste = TextInput(text='', multiline=False)
        layout.add_widget(self.rf_taste)

        btn_best_tt = Button(text="Travel Taste")
        btn_best_tt.bind(on_press=self.buttonClicked_TT)
        layout.add_widget(btn_best_tt)
        self.tt_taste = TextInput(text='', multiline=False)
        layout.add_widget(self.tt_taste)

        return layout

    def buttonClicked_LR(self,btn):
        y, X = taste()
        model = LogisticRegression()
        model = model.fit(X, y)
        a = int(self.age_taste.text)
        g = int(gender_converter(button_gender.text))
        i = int(self.income_taste.text)
        b = int(self.budget_taste.text)
        r1 = int(RecentVisit1_converter(button_rv1.text))
        r2 = int(RecentVisit2_converter(button_rv2.text))
        f = int(foreign_converter(button_foreign.text))
        p = int(purpose_converter(button_purpose.text))
        eat = int(EatingHabit_converter(button_eating.text))
        st = int(Stay_converter(button_stay.text))
        partner = int(PrefferedPartner_converter(button_partner.text))
        h = int(model.predict(np.array([1, a, g, i, b, r1, r2, f, eat, st, p, partner]).reshape(1, -1)))
        print(h)
        print(a , g , i , b , r1,r2,f,p,eat,st,partner)
        self.lr_taste.text = TravelTaste_Predictor(h)  # function call

    def buttonClicked_DT(self,btn):
        y, X = taste()
        clf = tree.DecisionTreeClassifier()
        clf = clf.fit(X, y)
        a = int(self.age_taste.text)
        g = int(gender_converter(button_gender.text))
        i = int(self.income_taste.text)
        b = int(self.budget_taste.text)
        r1 = int(RecentVisit1_converter(button_rv1.text))
        r2 = int(RecentVisit2_converter(button_rv2.text))
        f = int(foreign_converter(button_foreign.text))
        p = int(purpose_converter(button_purpose.text))
        eat = int(EatingHabit_converter(button_eating.text))
        st = int(Stay_converter(button_stay.text))
        partner = int(PrefferedPartner_converter(button_partner.text))
        h = int(clf.predict(np.array([1, a, g, i, b, r1, r2, f, eat, st, p, partner]).reshape(1, -1)))
        self.dt_taste.text = TravelTaste_Predictor(h) #function call

    def buttonClicked_SVM(self,btn):
        y, X = taste()
        clf = svm.SVC()
        clf.fit(X, y)
        a = int(self.age_taste.text)
        g = int(gender_converter(button_gender.text))
        i = int(self.income_taste.text)
        b = int(self.budget_taste.text)
        r1 = int(RecentVisit1_converter(button_rv1.text))
        r2 = int(RecentVisit2_converter(button_rv2.text))
        f = int(foreign_converter(button_foreign.text))
        p = int(purpose_converter(button_purpose.text))
        eat = int(EatingHabit_converter(button_eating.text))
        st = int(Stay_converter(button_stay.text))
        partner = int(PrefferedPartner_converter(button_partner.text))
        h = int(clf.predict(np.array([1, a, g, i, b, r1, r2, f, eat, st, p, partner]).reshape(1, -1)))
        self.svm_taste.text = TravelTaste_Predictor(h)  #function call

    def buttonClicked_RF(self,btn):
        y, X = taste()
        clf = RandomForestClassifier(n_estimators=10)
        clf = clf.fit(X, y)
        a = int(self.age_taste.text)
        g = int(gender_converter(button_gender.text))
        i = int(self.income_taste.text)
        b = int(self.budget_taste.text)
        r1 = int(RecentVisit1_converter(button_rv1.text))
        r2 = int(RecentVisit2_converter(button_rv2.text))
        f = int(foreign_converter(button_foreign.text))
        p = int(purpose_converter(button_purpose.text))
        eat = int(EatingHabit_converter(button_eating.text))
        st = int(Stay_converter(button_stay.text))
        partner = int(PrefferedPartner_converter(button_partner.text))
        h = int(clf.predict(np.array([1, a, g, i, b, r1, r2, f, eat, st, p, partner]).reshape(1, -1)))
        self.rf_taste.text = TravelTaste_Predictor(h) #function call

    def sendMail(self):
        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login("travelpredictor@gmail.com", "qwerty@123")

        # message to be sent
        message = "here is your travel taste prediction result " + self.tt_taste.text

        # sending the mail
        s.sendmail("travelpredictor@gmail.com",self.email.text, message)

        # terminating the session
        s.quit()

    def buttonClicked_TT(self,btn):
        r1 = int(TravelTaste_converter(self.lr_taste.text))
        r2 = int(TravelTaste_converter(self.rf_taste.text))
        r3 = int(TravelTaste_converter(self.svm_taste.text))
        r4 = int(TravelTaste_converter(self.dt_taste.text))
        results = np.array([r1, r2, r3, r4])
        counts = np.bincount(results)
        self.tt_taste.text = TravelTaste_Predictor(np.argmax(counts)) #function call
        self.sendMail()

if __name__ == '__main__':
    MyApp().run()
