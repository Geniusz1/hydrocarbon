from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.properties import NumericProperty, ObjectProperty


class HydrocarbonSandbox(Widget):

    segments_label = ObjectProperty(None)

    def removeSegment(self):
        if int(self.segments_label.text) <= 1:
            return
        self.segments_label.text = str(int(self.segments_label.text) - 1)
        print("remove")

    
    def addSegment(self):
        self.segments_label.text = str(int(self.segments_label.text) + 1)
        print("add")



class HydrocarbonApp(App):
    def build(self):
        return HydrocarbonSandbox()


if __name__ == '__main__':
    Config.set('graphics', 'width', '1200')
    Config.set('graphics', 'height', '700')
    HydrocarbonApp().run()
