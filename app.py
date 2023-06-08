from flask import Flask, request, render_template, redirect
import sqlite3

# init database

con = sqlite3.connect("pets.db", check_same_thread=False)
cur = con.cursor()


app = Flask(__name__)


@app.route("/")
@app.route("/pets", methods=["GET", "POST"])
@app.route("/pets/<id>", methods=["GET", "POST"])
def pets(id=-1):
    # /pets GET - get all pets
    # /pets/1 GET - get one pet
    if request.method == "GET":
        if id == -1:
            # get all pets
            res = cur.execute("SELECT * FROM pets")
        else:
            # get one pet
            res = cur.execute(f"SELECT * FROM pets WHERE id={id}")

        return render_template("pets.html", pets=res.fetchall())

    # /pets POST - add new pet
    # /pets/1 POST - update pet
    if request.method == "POST":
        name = request.form.get("name")
        type = request.form.get("type")
        age = request.form.get("age")
        if id == -1:
            res = cur.execute(f"INSERT INTO pets (name,type,age) VALUES ('{name}', '{type}', '{age}')")
        else:
            res = cur.execute(f"UPDATE pets SET name='{name}', type='{type}', age='{age}' WHERE id={id}")
        con.commit()
        return redirect("/pets")
            
            
            


if __name__ == '__main__':
    app.run(debug=True, port=9000)
