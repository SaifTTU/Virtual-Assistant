import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.config import Config
import subprocess

Config.set('graphics', 'resizable', True)

class ButtonApp(App):
    def build(self):
        btn=Button(text="Start Crystal",
            font_size ="20sp",
            background_normal='Sprite.png',
            background_down='Sprite-inverse.png',
            size =(32,32),
            size_hint=(.2,.2),
            pos=(300,250))
        btn.bind(on_press=self.callback)
        return btn
    def callback(self, event):
        subprocess.call("Virtual_assistant.py",shell=True)

root = ButtonApp()

if __name__ == '__main__':
    root.run()
