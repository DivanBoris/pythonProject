from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from datetime import datetime, date
from kivy.core.window import Window
from kivy.uix.behaviors import TouchRippleBehavior

Window.size = (430, 720)


class FirstWindow(Screen):
    def calc(self):
        data = {"Водительское удостоверение": date(2023, 7, 13),
                "Загранпаспорт №2": date(2031, 7, 13),
                "Загранпаспорт №1": date(2022, 12, 17),
                "Опито": date(2024, 4, 18),
                "НБЖС": date(2025, 2, 26),
                "Начальная подготовка": date(2025, 9, 2),
                "УЛМ": date(2025, 10, 11),
                "ОГУК": date(2024, 1, 10),
                "Норвежская медкомиссия": date(2024, 1, 10),
                "Прививка": date(2023, 4, 29),
                }
        a = []
        c = []
        [c.append(val) for key, val in data.items()]
        for key, val in data.items():
            if min(c) == val:
                e = key
        for key, val in data.items():
            if val <= date.today():
                a.append(key)
        b = ("\n".join(a))
        self.ids.FirstLabel.text = str(b)
        if len(a) == 0:
            self.ids.FirstLabel.text = f"Нет старых документов\nПРЕДУПРЕЖДАЮ\n{e} закончится\n{min(c)}"

class SecondWindow(Screen):
    pass

class DriverCardWindow(Screen):
    pass

class InternationalPassportOldWindow(Screen):
    pass

class InternationalPassportNewWindow(Screen):
    pass

class OpitoWindow(Screen):
    pass

class BasicSafetyWindow(Screen):
    pass

class SecurityTrainingWindow(Screen):
    pass

class IdWindow(Screen):
    pass

class OGUKWindow(Screen):
    pass

class NorwegianWindow(Screen):
    pass

class PfizerWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('source/my.kv')


class MyLayout(Widget):
    pass



class MyApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return kv


if __name__ == '__main__':
    MyApp().run()
