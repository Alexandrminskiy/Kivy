from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = FloatLayout()
        label1 = Label(text='Hello', size_hint=(0.3, 0.2), pos_hint={'center_x':0.5, 'center_y':0.8})
        label2 = Label(text='World', size_hint=(0.5, 0.7), pos_hint={'center_x':0.5, 'center_y':0.2})
        button = Button(text='World', size_hint=(0.2, 0.2), pos_hint={'center_x':0.1, 'center_y':0.1})

        button1 = Button(text='Йцукен', size=(50, 50), size_hint=(None,None), pos_hint={'center_x':0.9, 'center_y':0.1})

        layout.add_widget(label1)
        layout.add_widget(label2)
        layout.add_widget(button)
        layout.add_widget(button1)
        return layout

if __name__=='__main__':
    MyApp().run()
