from flask import Flask, render_template, request, redirect, session, flash, session
from db import connectToMySQL

app = Flask(__name__)

app.secret_key = "keep it secret"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results/<id>")
def results(id):
    db = connectToMySQL("survey")
    query = "SELECT * FROM survey WHERE id=" + id
    survey = db.query_db(query)
    return render_template("info.html", survey = survey)

@app.route("/", methods=["POST"])
def process_form():

    is_valid = True
    if len(request.form['name']) < 2:
        is_valid = False
        flash("Please enter a location name", "name")
    if len(request.form['location']) < 2:
        is_valid = False
        flash("Please enter a location name", "location")
    if len(request.form['language']) < 2:
        is_valid = False
        flash("Language should be at least 2 characters", "language")
    if len(request.form['comment']) > 120:
        is_valid = False
        flash("Comment can not exceed 120 characters", "comment")
    
    if is_valid == False:
        return redirect("/")
    else:
        db = connectToMySQL('survey')
        query = "INSERT INTO survey (name, location, language, comment, created_at, updated_at) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW());"
        data = {
            "name": request.form["name"],
            "location": request.form["location"],
            "language": request.form["language"],
            "comment": request.form["comment"]
        }
        flash("Successfully Imported!")
    id = db.query_db(query, data)
    return redirect("/results/" + str(id))

if __name__ == "__main__":
    app.run(debug=True)

