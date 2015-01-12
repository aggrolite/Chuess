# coding: utf-8
from flask import Flask, render_template, session, current_app, request
from os import urandom
import random

app = Flask(__name__, static_folder='static', static_url_path='')

positions = {
    'benko_gambit': 'rnbqkb1r/p2ppppp/5n2/1ppP4/2P5/8/PP2PPPP/RNBQKBNR',
    'caro-kann_defence': 'rnbqkbnr/pp1ppppp/2p5/8/4P3/8/PPPP1PPP/RNBQKBNR',
    'philidor_defence': 'rnbqkbnr/ppp2ppp/3p4/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R',
    'benoni_defence': 'rnbqkb1r/pp1ppppp/5n2/2p5/2PP4/8/PP2PPPP/RNBQKBNR',
    'sicilian_defence': 'rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR',
    'petrovs_defence': 'rnbqkb1r/pppp1ppp/5n2/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R',
    'scandinavian_defence': 'rnbqkbnr/ppp1pppp/8/3p4/4P3/8/PPPP1PPP/RNBQKBNR',
    'modern_defense': 'rnbqkbnr/pppppp1p/6p1/8/4P3/8/PPPP1PPP/RNBQKBNR',
    'pirc_defence': 'rnbqkbnr/ppp1pppp/3p4/8/4P3/8/PPPP1PPP/RNBQKBNR',
    'kings_gambit': 'rnbqkbnr/pppp1ppp/8/4p3/4PP2/8/PPPP2PP/RNBQKBNR',
    'queens_gambit_declined': 'rnbqkbnr/ppp2ppp/4p3/3p4/2PP4/8/PP2PPPP/RNBQKBNR',
    'birds_opening': 'rnbqkbnr/pppppppp/8/8/5P2/8/PPPPP1PP/RNBQKBNR',
    'ruy_lopez': 'r1bqkbnr/pppp1ppp/2n5/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R',
    'nimzo-indian_defence': 'rnbqk2r/pppp1ppp/4pn2/8/1bPP4/2N5/PP2PPPP/R1BQKBNR',
    'french_defence': 'rnbqkbnr/pppp1ppp/4p3/8/4P3/8/PPPP1PPP/RNBQKBNR',
    'giuoco_piano': 'r1bqk1nr/pppp1ppp/2n5/2b1p3/2B1P3/5N2/PPPP1PPP/RNBQK2R',
    'queens_pawn_opening': 'rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR',
    'gr�nfeld_defence': 'rnbqkb1r/ppp1pp1p/5np1/3p4/2PP4/2N5/PP2PPPP/R1BQKBNR',
    'alekhines_defence': 'rnbqkb1r/pppppppp/5n2/8/4P3/8/PPPP1PPP/RNBQKBNR',
    'old_indian_defence': 'rnbqkb1r/ppp1pppp/3p1n2/8/2PP4/8/PP2PPPP/RNBQKBNR',
    'english_opening': 'rnbqkbnr/pppppppp/8/8/2P5/8/PP1PPPPP/RNBQKBNR',
    'tarrasch_defense': 'rnbqkbnr/pp3ppp/4p3/2pp4/2PP4/2N5/PP2PPPP/R1BQKBNR',
    'dutch_defence': 'rnbqkbnr/ppppp1pp/8/5p2/3P4/8/PPP1PPPP/RNBQKBNR',
    'catalan_opening': 'rnbqkb1r/pppp1ppp/4pn2/8/2PP4/6P1/PP2PP1P/RNBQKBNR',
    'queens_gambit_accepted': 'rnbqkbnr/ppp1pppp/8/8/2pP4/8/PP2PPPP/RNBQKBNR',
    'scotch_game': 'r1bqkbnr/pppp1ppp/2n5/4p3/3PP3/5N2/PPP2PPP/RNBQKB1R',
    'slav_defence': 'rnbqkbnr/pp2pppp/2p5/3p4/2PP4/8/PP2PPPP/RNBQKBNR',
    'two_knights_defence': 'r1bqkb1r/pppp1ppp/2n2n2/4p3/2B1P3/5N2/PPPP1PPP/RNBQK2R',
    'kings_indian_attack': 'rnbqkbnr/ppp1pppp/8/3p4/8/5NP1/PPPPPP1P/RNBQKB1R',
    'kings_indian_defence': 'rnbqkb1r/pppppp1p/5np1/8/2PP4/8/PP2PPPP/RNBQKBNR'
}

@app.route("/")
def hello():

    return render_template('guess.html', pos=positions[ random.choice( positions.keys() ) ] )

app.secret_key = urandom(24)
app.logger.debug(app.secret_key)

if __name__ == "__main__":
    app.run(debug=True)
