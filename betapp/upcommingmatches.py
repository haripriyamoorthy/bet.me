import psycopg2
from .api import odds_json


conn = psycopg2.connect(user="postgres",password="root",database="betgame")
cur = conn.cursor()

i = cur.execute("SELECT * FROM betapp_upcommingmatchs;")

# for j in cur:
#     print(j)
query = """ INSERT INTO betapp_upcommingmatchs (sports_name,sports_title,start_time,home_team,away_team) VALUES (%{}s,%{}s,%{}s,%{}s,%{}s) """.format(odds_json[""])
cur.executemany(query)
