from kivy.app  import App
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Line
from kivy.uix.widget import Widget

# class MyLabel(Label):
#     def __init__(self, text):
#         super().__init__()
#         self.text = text
#         def on_touch_down(self, touch):
#             print('DOWN', touch)
#         def on_touch_up(self, touch):
#             print('UP', touch)
#         def on_touch_move(self, touch):
#             print('MOVE', touch)
#
#
# class MyApp(App):
#     def build(self):
#         self.thislabel = MyLabel('hi')
#         return self.thislabel



class MyWidget(Widget):
    def on_touch_down(self, touch):
        touch.ud['line'] = Line(points=(touch.x, touch.y))
        self.canvas.add(touch.ud['line'])

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]
    # def on_touch_down(self, touch):
    #     self.canvas.add(Rectangle(pos=(touch.x, touch.y), size=(50, 50)))

class MyApp(App):
    def build(self):
        return MyWidget()

if __name__=='__main__':
    MyApp().run()
