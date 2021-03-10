from flask import Flask, render_template
from threading import Thread
import logging

app = Flask('')

# make ping log go away
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

#PAGES
# ---------------------------------------

@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/discord-oni')
@app.route('/oni')
def discord_oni():
    return render_template('oni.html')


# ---------------------------------------


def run():
    app.run(host='0.0.0.0', port=8080)


def online():
    t = Thread(target=run)
    t.start()


if __name__ == "__main__":
    online()