xo00	from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class BharatBrowser(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        
        nav_bar = BoxLayout(size_hint_y=0.1)
        
        self.url_bar = TextInput(
            text='https://www.google.co.in',
            multiline=False,
            size_hint_x=0.8
        )
        
        go_btn = Button(
            text='Search',
            size_hint_x=0.2,
            background_color=(0.1, 0.6, 0.3, 1)
        )
        go_btn.bind(on_press=self.open_url)
        
        nav_bar.add_widget(self.url_bar)
        nav_bar.add_widget(go_btn)
        
        self.add_widget(nav_bar)

    def open_url(self, instance):
        print(f"Loading: {self.url_bar.text}")

class MainApp(App):
    def build(self):
        self.title = "Bharat Browser"
        return BharatBrowser()

if __name__ == '__main__':
    MainApp().run()

