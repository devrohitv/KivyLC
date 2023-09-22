import os
import json
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
import firebase_admin
from firebase_admin import credentials, storage

with open("fireadmin.json") as f:
    d = json.load(f)
cred = credentials.Certificate(d)
firebase_admin.initialize_app(cred, {"storageBucket": "classmate-classes.appspot.com"})


class MyData(BoxLayout):
    source_file = StringProperty("")

    def show_data(self):
        #self.upload_file()
        self.download_file()
        self.crud()

    try:
        def upload_file(self):
            bucket = storage.bucket()
            blob = bucket.blob("image.jpg")
            blob.upload_from_filename("file/my.jpg")
            print(f"File {'my.jpg'} uploaded to {'image.jpg'}.")
            blob.make_public()
            print(blob.public_url)

        def download_file(self):
            bucket = storage.bucket()
            blob = bucket.blob("image.jpg")
            blob.download_to_filename("file/adminimage.jpg")
            print(f"File {'image.jpg'} downloaded to {'file/adminimage.jpg'}.")

    except Exception as e:
        print(e)

    def crud(self):
        self.source_file = "file/adminimage.jpg"

        try:
            os.remove("file/adminimage.jpg")
            print("successfully deleted")
        except Exception as g:
            print(g)


class MyApp(App):
    def build(self):
        return MyData()


MyApp().run()
