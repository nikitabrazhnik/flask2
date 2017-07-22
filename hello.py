from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World!"


@app.route("/i")
def index_i():
    return "Hello, World 2!"


if __name__ == '__main__':
    app.run()