from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock, mainthread
import speech_recognition as sr
import threading, socket


class TranslatePage(App):

    def GetAudio(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
        audiobytes = audio.get_raw_data()

        return audiobytes

    def build(self):
        main_layout = BoxLayout(orientation="vertical")
        info_text = Label(text="Press button to activate.")
        main_layout.add_widget(info_text)

        activate_button = Button(text="Activate")
        activate_button.bind(on_press=self.on_press_button)
        main_layout.add_widget(activate_button)
        return main_layout

    def on_press_button(self, instance):
        print("starting")
        HOST = '127.0.0.1'
        PORT = 6000
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            while True:
                s.sendall(self.GetAudio())


if __name__ == '__main__':
    app = TranslatePage()
    app.run()
