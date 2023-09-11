from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from firebase import firebase


class MyData(BoxLayout):
    def show_data(self):
        data = firebase.FirebaseApplication('https://classmate-classes-f9057-default-rtdb.firebaseio.com/', None)

        raw_data = data.get("Mathematics", "")
        self.ids.button.text = str(raw_data)


class MyApp(App):
    def build(self):
        return MyData()

MyApp().run()
