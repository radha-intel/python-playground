from flask import Flask
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def data():
    url = 'http://10.223.163.26:7000/image/google/builds'
    payload = {'platform': 'brya', 'hardware' : 'brya'}
    req = requests.get(url, params=payload)
    print(req.json())
    return f"<h1>{req.content}</h1>"

if __name__ == "__main__":
    app.run()