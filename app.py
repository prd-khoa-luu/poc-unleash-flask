import os

from flask import Flask
from UnleashClient import UnleashClient


token = os.getenv("CLIENT_ACCESS_TOKEN", default=None)
headers = {'Authorization': token} if token else {}

client = UnleashClient("https://ol-unleash.herokuapp.com/api", "Unleash PoC", custom_headers=headers)
client.initialize_client()

app = Flask(__name__)


@app.route("/")
def index():
    # NOTE: param `default_value` is deprecated! Use the fallback_function on the main is_enabled() method.
    if client.is_enabled("index-hello"):
        return "Hello World!"
    else:
        return "Goodbye World!"


if __name__ == '__main__':
    try:
        app.run()
    finally:
        client.destroy()
