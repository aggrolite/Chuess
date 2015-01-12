from flask import Flask, render_template, session, current_app, request
from os import urandom
import random

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route("/")
def hello():
    positions = {
            'lopez': 'r1bqkbnr/pppp1ppp/2n5/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R',
            'italian': 'r1bqkbnr/pppp1ppp/2n5/4p3/2B1P3/5N2/PPPP1PPP/RNBQK2R',
            'queens_gambit': 'rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR'
    }
    if 'chuess' not in session:
        session['chuess'] = '';
        app.logger.debug('creating new session cookie')

    return render_template('guess.html', pos=positions[ random.choice( positions.keys() ) ] )

app.secret_key = urandom(24)
app.logger.debug(app.secret_key)

if __name__ == "__main__":
    app.run(debug=True)
