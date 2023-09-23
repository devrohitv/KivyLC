import os
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
import firebase_admin
from firebase_admin import credentials, storage
from jnius import autoclass
from android.permissions import check_permission, request_permissions, Permission

Environment = autoclass('android.os.Environment')
path = Environment.getExternalStorageDirectory().getAbsolutePath()

cred = credentials.Certificate("fireadmin.json")
firebase_admin.initialize_app(cred, {"storageBucket": "classmate-classes.appspot.com"})


class MyData(BoxLayout):
    source_file = StringProperty("")

    def down_data(self):
        # self.crud()
        # self.upload_file()
        self.download_file()

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
            blob.download_to_filename(f"{path}/adminimage.jpg")
            print(f"File {'image.jpg'} downloaded to {'path/adminimage.jpg'}.")
            w = f"File {'image.jpg'} downloaded to {'path/adminimage.jpg'}."
            self.ids.notice.text = w

    except Exception as e:
        print(e)

    def show_image(self):
        self.source_file = f"{path}/adminimage.jpg"

    def delete(self):
        try:
            os.remove("file/adminimage.jpg")
            print("successfully deleted")
            self.ids.notice.text = "successfully deleted"
        except Exception as g:
            print(g)
            self.ids.notice.text = g


class MyApp(App):
    def build(self):
        return MyData()

    def on_start(self):

        if not check_permission(Permission.READ_EXTERNAL_STORAGE) or not check_permission(
                Permission.WRITE_EXTERNAL_STORAGE):
            # Request permissions if not granted
            permissions = [Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE]
            request_permissions(permissions)
        else:
            # Permissions are already granted, you can proceed with your app logic
            pass


MyApp().run()
