from flask import Flask, request, redirect, url_for
from flask import render_template
from config import Config
from game_of_life import GameOfLife
from project.forms import HomeForm


app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods=["GET", "POST"])
def index():
    height = None
    width = None
    form = HomeForm()
    if form.validate_on_submit():
        height = form.height.data
        width = form.width.data
        GameOfLife(width, height)
        return redirect(url_for('index'))

    return render_template("index.html", form=form)





@app.route('/live', methods=["GET", "POST"])
def live():
    new_game = GameOfLife()
    if new_game.counter > 0:
        new_game.form_new_generation()
    new_game.counter += 1
    return render_template("live.html", new_game=new_game)


if __name__ =="__main__":
    app.run(debug=True)


# app.run(host='0.0.0.0', post=5000)
