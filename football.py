import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

db = "database.db"


@app.route("/")
def index():
  try:
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from tournaments")
    rows = cur.fetchall()
    conn.close()
    return render_template("index.html",rows=rows)
  except:
    return render_template("error.html")


@app.route('/matches/<id>')
def matches(id):
  try:
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from matches WHERE tournament_id =" + id)
    matches = cur.fetchall()
    conn.close()
    return render_template("matches.html",matches=matches)
  except:
    return render_template("error.html")


@app.route('/scorers/<id>')
def scorers(id):
  try:
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from goal_scorers WHERE match_id =" + id)
    scorers = cur.fetchall()
    cur.execute("select * from matches WHERE id =" + id)
    match = cur.fetchall()
    conn.close()
    return render_template("scorers.html",scorers=scorers,match=match)
  except:
    return render_template("error.html")