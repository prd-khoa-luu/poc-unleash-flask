from flask import Flask
from UnleashClient import UnleashClient


client = UnleashClient("https://ol-unleash.herokuapp.com/api", "Unleash PoC")
client.initialize_client()

app = Flask(__name__)


@app.route("/")
def index():
    if client.is_enabled("index-hello", default_value=True):
        return "Hello World!"
    else:
        return "Goodbye World!"


if __name__ == '__main__':
    try:
        app.run()
    finally:
        client.destroy()
