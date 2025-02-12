from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask App!"

@app.route('/data')
def data():
    host = os.environ.get("MYSQL_HOST")
    user = os.environ.get("MYSQL_USER")
    password = os.environ.get("MYSQL_PASSWORD")
    database = os.environ.get("MYSQL_DATABASE")
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    cursor = connection.cursor()
    cursor.execute("SELECT DATABASE();")
    db_name = cursor.fetchone()
    return jsonify({"Connected to": db_name[0]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)