from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/from-db")
def from_db():
    conn_string = "host='localhost' dbname='my_database' user='postgres' password='secret'"
	conn = psycopg2.connect(conn_string)
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM pg_stats limit 1")
	records = cursor.fetchall()
	return str(records)

if __name__ == "__main__":
    app.run()

