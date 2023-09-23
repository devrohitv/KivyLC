import os
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
import firebase_admin
from firebase_admin import credentials, storage

d = {
  "type": "service_account",
  "project_id": "classmate-classes",
  "private_key_id": "bb6fe91c517607d1274e1b21195f596bc1a6fbae",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDa4I9JJP/TKyda\n7mjN0i7o/d9+8GqhZy4Wn4aNj5FJiiGjtLj9SpqXVQQ6+e8wyBZO4RQ+1jjoiCm2\ndQD2644dzc3pkspJVUnN2C5LfwV8H8Z1OndICwJg95MgY+lsWXlwZiRQiyyFU4UU\nPOOQ22/Ovm/w0ZtnjMTPny4V9Zgsm9Gm4Z5YxPXv/xxHj7rNGjyJP9RHx2j+Iciq\nr8K10YRIwPcyfhlkaUNIyxiKGS8Oyy4nsanA/7hA7h6fBCKHOdS3ea6QEh8WzhvU\neRgEed421gEdYVLS3+WKus78TM3SODCz2UQeMdvJ4jmEq7caDtUq2cLjU1ukWMvW\ntUAg5BfvAgMBAAECggEABKkec/TFO8Zh9qY39hYBKLXrMeVFp/0t9o5cC5ygf9vg\nnn9FJyOVCh7l0amrxbKlAvX4++OM36qylK+GHzvh0VGmDlCxXQFjam4tgi8Iu11j\n2PAvRQny+YScDecCu+tl0hZitJJaFtax8T3grJ93kIPul0anU/uj3zXpAc+yd1Sp\n+7zakSMJX9tEbWpXpsoVyAPec8yyWeyse7oqQXpdVBsNaJz8KecRUGPmfPHPYFj1\nJ4ssjSF1scg5Varc1GLgV9mTdnItoVt1y2qbADZCBX4Cj4RrBc2jPRQ/IdJ1OwSC\nV/uRX7PXpO2kcruGCVJ7h2KqMqph3wtwBpHF6GuqIQKBgQDv5zJqidCMtBnatJL7\nLQTwsk6OgENve/PzmUS2wchbTBXYIK0iztAMSC9n+WGQMBHweQjcMDmXYbeBoPgC\nzqovvrJ3pzbiW0REyj9wid4VWAE57HSrbxuNVQXas5n7RN8focuHA/pr9k4rbjqm\nLR+XMtrWtOQ0JmlVge0/ytmAIQKBgQDpkDOYVscweg7Ys2hrZimN3LGH4YmiQeBX\nysOQGbZHE+V0bwbYhQu81aRs/l0fWHiTWge4I1iND6iDJXPFmlio91NPfMfHIvxf\n6fT39C+xEXTq3dOyoY8jJ2aVbev03HYTo+j74iJG3kHkvkz4MEGLl0inJRBONm0c\nQexT88rWDwKBgQDtVGkZ4JDCQYG6TR2DArx6acsxSk5sQdHK0Xua2QYe25xYnarq\nXnKPU/IiCCGuhP+aSAKt4b93tSHXSalRDaZraVog6Plw4R0eeH5eFOXxc4hzBys8\nVcSKAuyxuS/B1hZtsqAoR5U7rQUUDg5TSxyPda3s7jM8LCvUfZ55l3GoQQKBgGDa\nvJqaucU/iHKSi2WmGutKLpCDlZikqsydN9XE49K7zHYpKHSXT5PCIIpWPPWnsXCh\nb/wLJEhyytV/rW+vHr8KuRCIVSweNPvtP/mm2DQcYhiXXpd/6aSRTTgAOk3zMj/Y\nw9/YGZC70CV0SOTO1g9179noQ8e7SCnkqITz3xQ/AoGAf6W+vM5glkzb0Rs3Zl0M\nlJoY6D26vQoOwY45Vcu30ClTPceilu/nTeiwkwDlr/yiMuMzrsImJTSb77TMvax/\nAynE9TrvYSvEkgI7gfhSVHB3lSgTKdo/OacXCXfzdOx5wfmX/UkVwl5DcHi+ocFv\ncQ8r3GmAouLJzf7qRJxhzQo=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-x8086@classmate-classes.iam.gserviceaccount.com",
  "client_id": "102132813188077862362",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-x8086%40classmate-classes.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

cred = credentials.Certificate(d)
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
            blob.download_to_filename("file/adminimage.jpg")
            print(f"File {'image.jpg'} downloaded to {'file/adminimage.jpg'}.")
            w = f"File {'image.jpg'} downloaded to {'file/adminimage.jpg'}."
            self.ids.notice.text = w

    except Exception as e:
        print(e)

    def show_image(self):
        self.source_file = "file/adminimage.jpg"

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


MyApp().run()
