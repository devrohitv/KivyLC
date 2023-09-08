import json
import pyrebase
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

file = []


def image_load(lind_id, class_):
    global file
    file.append(lind_id)
    storage = firebase_.storage()
    storage.download(f"{lind_id}/{class_}", f"chapter_visual_data/{lind_id}.pdf")

