import os
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
import firebase_admin
from firebase_admin import credentials, storage
from android.permissions import check_permission, request_permissions, Permission
from android import mActivity

context = mActivity.getApplicationContext()
result = context.getExternalFilesDir("images")   
if result:
    storage_path = str(result.toString())


cred = credentials.Certificate("fireadmin.json")
firebase_admin.initialize_app(cred, {"storageBucket": "classmate-classes.appspot.com"})


class MyData(BoxLayout):
    source_file = StringProperty("")
    image_file = StringProperty("")

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
            blob.download_to_filename(f"{storage_path}/adminimage.jpg")
            print(f"File {'image.jpg'} downloaded to {'path/adminimage.jpg'}.")
            w = f"File {'image.jpg'} downloaded to {'path/adminimage.jpg'}."
            self.ids.notice.text = w

    except Exception as e:
        print(e)

    def show_image(self):
        self.image_file = "https://storage.googleapis.com/classmate-classes.appspot.com/image.jpg"
        self.source_file = f"{storage_path}/adminimage.jpg"

    def delete(self):
        try:
            path = f"{storage_path}/adminimage.jpg"
            file = os.path.isfile(path)
            if file:
                os.remove(f"{storage_path}/adminimage.jpg")
                print("successfully deleted")
                self.ids.notice.text = "successfully deleted"
            else:
                self.ids.notice.text = "file does not exist"
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
