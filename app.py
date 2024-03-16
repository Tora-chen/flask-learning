from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route("/")
def index():
    name = request.args.get("name", "world")
    return render_template("index.html", name=name)


@app.route("/greet")
def greet():
    name = request.args.get("name", "world")
    return render_template("greet.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)
