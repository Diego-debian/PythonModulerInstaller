from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.app import App
import subprocess

class Instaler(App):
    def build(self):
        self.positionLabel = 1
        self.img = Image()
        self.img.source = "./Images/Burble/Burble.zip"
        self.img.pos_hint={'center_x':0.5,'center_y':0.5}
        self.img.size_hint_x = .55
        self.img.size_hint_y = .4
        self.img.anim_delay = 0.6
        self.rl = RelativeLayout()
        self.rl.add_widget(self.img)
        self.Labels()
        self.Buttons()        
        return self.rl
    
    def Labels(self):        
        self.lb0 =Label(pos_hint={'center_x':0.5,'center_y':0.9}, font_size = "32 sp")
        self.lb1 =Label(pos_hint={'center_x':self.positionLabel,'center_y':0.1}, font_size = "32 sp")
        self.lb0.text = "---CODE INSTALLER---"
        self.lb1.text = "I'm very happy for that you install the python modules with my software, just relax. By Diego Parra "
        self.rl.add_widget(self.lb0)
        self.rl.add_widget(self.lb1)        
        animation1 = Animation(color=[1,1,0,0.7], duration = 20) 
        animation1.repeat= True
        animation2 = Animation(color=[1,0,0,0.7], duration = 10) 
        animation2.repeat = True
        animation1.start(self.lb0)
        animation2.start(self.lb1)
        Clock.schedule_interval(self.animationLabel, .1)
        
    def animationLabel(self, t):
        if self.positionLabel <= -2:
            self.positionLabel = 2
        if self.positionLabel >= -2:
            self.positionLabel = self.positionLabel - 0.01
            self.lb1.pos_hint = {'center_x':self.positionLabel,'center_y':0.1}
        
        
    def Buttons(self):
        self.bt1 = Button(size_hint_x=.2, size_hint_y=.1, pos_hint={'center_x':0.12,'center_y':0.65}, text="install numpy")
        self.bt2 = Button(size_hint_x=.2, size_hint_y=.1, pos_hint={'center_x':0.12,'center_y':0.55}, text="install pandas")
        self.bt3 = Button(size_hint_x=.2, size_hint_y=.1, pos_hint={'center_x':0.12,'center_y':0.45}, text="install gnuplot")
        self.bt4 = Button(size_hint_x=.2, size_hint_y=.1, pos_hint={'center_x':0.12,'center_y':0.35}, text="install matplotlib")
        self.bt5 = Button(size_hint_x=.2, size_hint_y=.1, pos_hint={'center_x':0.86,'center_y':0.65}, text="install jupyter")
        self.bt6 = Button(size_hint_x=.2, size_hint_y=.1, pos_hint={'center_x':0.86,'center_y':0.55}, text="install googlesearch")
        self.bt7 = Button(size_hint_x=.2, size_hint_y=.1, pos_hint={'center_x':0.86,'center_y':0.45}, text="install webview")
        self.bt8 = Button(size_hint_x=.2, size_hint_y=.1, pos_hint={'center_x':0.86,'center_y':0.35}, text="install pyserial")
        
        self.rl.add_widget(self.bt1)
        self.rl.add_widget(self.bt2)
        self.rl.add_widget(self.bt3)
        self.rl.add_widget(self.bt4)
        self.rl.add_widget(self.bt5)
        self.rl.add_widget(self.bt6)
        self.rl.add_widget(self.bt7)
        self.rl.add_widget(self.bt8)
        self.bt1.bind(on_press=self.acbt1)
        self.bt2.bind(on_press=self.acbt2)
        self.bt3.bind(on_press=self.acbt3)
        self.bt4.bind(on_press=self.acbt4)
        self.bt5.bind(on_press=self.acbt5)
        self.bt6.bind(on_press=self.acbt6)
        self.bt7.bind(on_press=self.acbt7)
        self.bt8.bind(on_press=self.acbt8)

    #Install numpy button 
    def acbt1(self, *args):
        try:
            import numpy
            print("Numpy is install")
        except: 
            numpy = "pip3 install numpy"
            installer = subprocess.call(numpy, shell= True)
            print("Returned value:", installer)
        self.bt1.unbind()

        
    #Install pandas button 
    def acbt2(self, *args):
        try:
            import pandas
            print("pandas is install")
        except: 
            pandas = "pip3 install pandas"
            installer = subprocess.call(pandas, shell= True)
            print("Returned value:", installer)
        self.bt2.unbind()

    #Install gnuplot button 
    def acbt3(self, *args):
        try:
            from pygnuplot import gnuplot
            print("gnuplot is install")
        except: 
            gnuplot = "pip3 install py-gnuplot"
            installer = subprocess.call(gnuplot, shell= True)
            print("Returned value:", installer)
        self.bt3.unbind()

    #Install matplotlib button 
    def acbt4(self, *args):
        try:
            from matplotlib import pyplot
            print("matplotlib is install")
        except: 
            matplotlib = "pip3 install matplotlib"
            installer = subprocess.call(matplotlib, shell= True)
            print("Returned value:", installer)
        self.bt4.unbind()

    #Install jupyter button 
    def acbt5(self, *args):
        try:
            import jupyter
            print("jupyter is install")
        except: 
            jupyter = "pip3 install jupyter notebook"
            installer = subprocess.call(jupyter, shell= True)
            print("Returned value:", installer)
        self.bt5.unbind()
         
    #Install google search  button 
    def acbt6(self, *args):
        try:
            import google
            print("Google is install")
        except: 
            google = "pip3 install google"
            installer = subprocess.call(jupyter, shell= True)
            print("Returned value:", installer)
        self.bt6.unbind()

    #Install webview button 
    def acbt7(self, *args):
        try:
            import webview
            print("Webview is install")
        except: 
            webview = "pip3 install pywebview"
            installer = subprocess.call(webview, shell= True)
            print("Returned value:", installer)
        self.bt7.unbind()

    #Install webview button 
    def acbt8(self, *args):
        try:
            import serial
            print("pyserial install")
        except: 
            pyserial = "pip3 install pyserial"
            installer = subprocess.call(pyserial, shell= True)
            print("Returned value:", installer)
        self.bt8.unbind()
