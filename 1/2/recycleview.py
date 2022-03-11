from kivy.app import App
from kivy.uix.recycleview import RecycleView

class RV(RecycleView):
    def __init__(self):
        super().__init__()
        content = ['hello', 'this is a dtring', 'another string']
        self.data = [{'text':item} for item in content]

class MyApp(App):
    def build(self):
        return RV()

MyApp().run()
