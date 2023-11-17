from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

KV = '''
MDScreen:
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        MDTopAppBar:
            title: "Egg Catcher"
    MDRectangleFlatButton:
        text:"Savjot"
        pos_hint: {'center_x':0.5, 'center_y':0.5}
'''

class MainAPP(MDApp):
    def __init__(self):
        super().__init__()
        self.kvs = Builder.load_string(KV)

    def build(self):
        screen = Screen()
        screen.add_widget(self.kvs)
        return screen
ma = MainAPP()
ma.run()