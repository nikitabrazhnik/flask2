from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World!"


@app.route("/i")
def index_i():
    return "Hello, World 2!"


<<<<<<< HEAD
#edde
=======
#e
>>>>>>> 93dc51fb1113d06c17cc894d72964cec3eefba66
if __name__ == '__main__':
    app.run(port=5000, debug=True)