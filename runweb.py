from flask import Flask, render_template
import functions

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/view")
def view():
    return render_template("view.html", content=functions.get_list_recipe())


@app.route("/incl")
def incl():
    return render_template("incl.html")


@app.route("/rand")
def rand():
    return render_template("rand.html", content=functions.get_random())


@app.route("/add")
def add():
    return render_template("add.html")


@app.route("/del")
def delete():
    return render_template("del.html")


if __name__ == "__main__":
    app.run(debug=True)
    