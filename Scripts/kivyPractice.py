
import kivy
kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.label import Label


class KivyPractice(App):
    def build(self):
        return Label()


if __name__ == '__main__':
    KivyPractice().run()
