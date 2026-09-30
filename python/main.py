from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

def create_connection():
    connection = mysql.connector.connect(
        host=os.environ.get('MYSQL_HOST'),
        user=os.environ.get('MYSQL_USER'),
        password=os.environ.get('MYSQL_PASSWORD'),
        database=os.environ.get('MYSQL_DATABASE')
    )
    return connection

@app.route("/")
def home():
    return "Welcome to the Flask MySQL App!"

@app.route("/students")
def get_students():
    connection = create_connection()
    
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students")
    
    students = cursor.fetchall()
    
    cursor.close()
    connection.close()
    
    return jsonify(students)

if __name__ == "__main__":
    app.run(host="0.0.0.0", 
            port=5000
            )
