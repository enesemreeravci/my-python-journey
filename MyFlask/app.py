from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

DATABASE = "users.db"

def create_table():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   username TEXT NOT NULL,
                   email TEXT NOT NULL,
                   password TEXT NOT NULL
                   )
                   """)
    connection.commit()
    connection.close()

@app.route("/")
def home():
    return redirect("/register")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()

        cursor.execute("""
                INSERT INTO users (username, email, password)
                VALUES (?, ?, ?)
                """, (username, email, password))
        
        connection.commit()
        connection.close()

        return redirect("/users")
    
    return render_template("register.html")

@app.route("/delete/<int:user_id>", methods=["POST"])
def delete(user_id):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute(
            "DELETE FROM users WHERE id = ?",
            (user_id,)
        )

    connection.commit()
    connection.close()

    return redirect("/users")
    
@app.route("/users")
def user():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("SELECT id, username, email FROM users")
    users = cursor.fetchall()

    connection.close()

    return render_template("users.html", users=users)

if __name__ == "__main__":
    create_table()
    app.run(debug=True)