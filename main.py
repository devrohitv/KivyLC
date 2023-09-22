import os
# from kivy.clock import Clock
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from pyrebase import pyrebase
import json

with open('serviceAccount.json', 'r') as file_obj:
    f = json.load(file_obj)
config = {
    "apiKey": "AIzaSyAxiO8FrPTUF4I7PSR6i8ZlqXWJMeVyYxQ",
    "authDomain": "classmate-classes-f9057.firebaseapp.com",
    "databaseURL": "https://classmate-classes-f9057-default-rtdb.firebaseio.com",
    "projectId": "classmate-classes-f9057",
    "storageBucket": "classmate-classes-f9057.appspot.com",
    "messagingSenderId": "286165438643",
    "appId": "1:286165438643:web:658c70f981cf5b8cabe0c6",
    "measurementId": "G-18KW9VP3P6",
    "serviceAccount": f,
    "databaseUrl": "https://classmate-classes-f9057-default-rtdb.firebaseio.com/"
}
firebase_ = pyrebase.initialize_app(config)


class MyData(BoxLayout):
    source_file = StringProperty("")

    def show_data(self):
        storage = firebase_.storage()
        # storage.child('hello').put('C:/Users/user/Downloads/GITHUBERROR.jpg')
        storage.download("hello", f"{'file'}/{'my.jpg'}")
        # url = storage.child("hello").get_url(user["idToken"])
        # url = storage.child("hello").get_url(["idToken"])
        # print(url)

        print("downloaded")

        self.source_file = "file/my.jpg"

        try:
            os.remove("file/my.jpg")
            print("successfully deleted")
        except Exception as g:
            print(g)


class MyApp(App):
    def build(self):
        return MyData()


MyApp().run()
