import csv
import sqlite3
from datetime import datetime


#opening connection to the database/ creates database if not found
conn = sqlite3.connect("database.db")
cur = conn.cursor()


conn.execute("DROP TABLE IF EXISTS goal_scorers")
conn.execute("DROP TABLE IF EXISTS matches")
conn.execute("DROP TABLE IF EXISTS tournaments")
print("table dropped successfully")

conn.execute("CREATE TABLE tournaments (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
conn.execute("CREATE TABLE matches (id INTEGER PRIMARY KEY AUTOINCREMENT, home_team TEXT, away_team TEXT, home_score INTEGER, away_score INTEGER, tournament INTEGER, tournament_id INTEGER, date DATE, match_city TEXT, match_country TEXT, FOREIGN KEY(tournament_id) REFERENCES tournament(id) )")
conn.execute("CREATE TABLE goal_scorers (id INTEGER PRIMARY KEY AUTOINCREMENT, home_team TEXT, away_team TEXT, team_scored TEXT, scorer TEXT, minute INTEGER, match_id INTEGER, date DATE ,FOREIGN KEY(match_id) REFERENCES matches(id) )")

tournaments_list = ["FIFA World Cup", "FIFA World Cup qualification", "UEFA Euro", "UEFA Euro qualification", "UEFA Nations League"]
id = 1
for i in range(5):
  tournament = tournaments_list[i]
  cur.execute('INSERT INTO tournaments VALUES (?,?)', (id,tournament))
  conn.commit()
  id += 1


with open("results.csv", newline = "") as f:
  reader = csv.reader(f, delimiter=",")
  next(reader)
  for row in reader:
    print(row)

    home_team = row[1]
    away_team = row[2]
    home_score = int(row[3])
    if(row[0][-5] == "-"):
      date = datetime.strptime(row[0], '%d-%m-%Y')
    else:
      date = datetime.strptime(row[0], '%m/%d/%Y')
    away_score = int(row[4])
    tournament = row[5]
    tournament_id = tournaments_list.index(tournament) + 1
    match_city = row[6]
    match_country = row[7]

    cur.execute('INSERT INTO matches VALUES (NULL,?,?,?,?,?,?,?,?,?)', (home_team, away_team, home_score, away_score, tournament,tournament_id,date,match_city,match_country))
    conn.commit()

cur.execute('select * from matches')
matches = cur.fetchall()

with open("goalscorers.csv", newline = "") as f:
  reader = csv.reader(f, delimiter=",")
  next(reader)
  for row in reader:
    #print(row)

    home_team = row[1]
    away_team = row[2]
    team_scored = row[3]
    scorer = row[4]
    minute = int(row[6])
    if(row[0][-5] == "-"):
      date = datetime.strptime(row[0], '%d-%m-%Y')
    else:
      date = datetime.strptime(row[0], '%m/%d/%Y')

    cur.execute('SELECT id FROM matches WHERE home_team = ? AND away_team = ? AND date = ?',(home_team, away_team, date))
    match = cur.fetchone()
    if match:
        match_id = match[0]
    else:
        match_id = 0
    

    cur.execute('INSERT INTO goal_scorers VALUES (NULL,?,?,?,?,?,?,?)', (home_team, away_team, team_scored, scorer, minute,match_id,date))
    conn.commit()
    

print("data parsed successfully")
conn.close()




