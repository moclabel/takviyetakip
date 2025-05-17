from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button

class SupplementApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        layout.add_widget(Label(text="Takviye Takip Uygulaması"))
        checkbox = CheckBox()
        layout.add_widget(checkbox)
        
        button = Button(text="Takviye Kaydet")
        layout.add_widget(button)
        
        return layout

if __name__ == '__main__':
    SupplementApp().run()
