import pickle
import socket
from _thread import *

import pyttsx3
import speech_recognition as sr
from deep_translator import GoogleTranslator
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.logger import Logger, LOG_LEVELS


class TranslatePage(App):

    def GetAudio(self):
        Logger.debug("Application: Getting microphone")
        text = None
        while text is None:
            with sr.Microphone(device_index=2) as source:
                audio = self.r.listen(source)
            text = self.r.recognize_sphinx(audio)
        Logger.debug(text)
        data = pickle.dumps([self.language, text])
        return data

    def build(self):
        # Logger.setLevel(LOG_LEVELS["debug"])

        self.r = sr.Recognizer()
        self.language = None
        self.capibilities = {
            "languages": GoogleTranslator.get_supported_languages()
        }
        self.main_layout = BoxLayout(orientation="vertical")
        self.language_adjust = DropDown()
        for language in self.capibilities['languages']:
            btn = Button(text=language, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.language_adjust.select(btn.text))
            self.language_adjust.add_widget(btn)

        self.language_adjust_button = Button(text='Change Language')
        self.language_adjust_button.bind(on_release=self.language_adjust.open)
        self.language_adjust.bind(on_select=self.select_language)
        self.main_layout.add_widget(self.language_adjust_button)

        adjust_noise = Button(text="Adjust for background noise")
        adjust_noise.bind(on_press=self.adjust_background_audio)
        self.main_layout.add_widget(adjust_noise)

        activate_button = Button(text="Activate")
        activate_button.bind(on_press=self.start_audio)
        self.main_layout.add_widget(activate_button)
        return self.main_layout

    def start_audio(self, instance):
        Logger.debug("starting")
        HOST = '127.0.0.1'
        PORT = 6000
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        start_new_thread(self.audio_processing, (s,))
        start_new_thread(self.speech, (s,))

    def adjust_background_audio(self, instance):
        with sr.Microphone(device_index=2) as source:
            self.r.adjust_for_ambient_noise(source, duration=1)

    def audio_processing(self, s):
        with s:
            while True:
                byteaudio = self.GetAudio()
                s.sendall(byteaudio)

    def speech(self, s):
        engine = pyttsx3.init()
        with s:
            while True:
                data = str(s.recv(1024))
                Logger.debug('recived: '+data)
                engine.say(data)
                engine.runAndWait()

    def select_language(self, instance, x):
        setattr(self.language_adjust_button, 'text', x)
        self.language = x


if __name__ == '__main__':
    app = TranslatePage()
    app.run()
