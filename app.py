import os

from flask import Flask, render_template
from UnleashClient import UnleashClient


token = os.getenv("CLIENT_ACCESS_TOKEN", default=None)
headers = {'Authorization': token} if token else {}

client = UnleashClient("https://ol-unleash.herokuapp.com/api", "Unleash PoC", custom_headers=headers)
client.initialize_client()

app = Flask(__name__)


@app.route("/")
def index():
    # NOTE: param `default_value` is deprecated! Use the fallback_function on the main is_enabled() method.
    greeting = "HELLO WORLD" if client.is_enabled("index-hello") else "GOODBYE WORLD"

    return render_template("index.html", greeting=greeting)

if __name__ == '__main__':
    try:
        app.run()
    finally:
        client.destroy()
