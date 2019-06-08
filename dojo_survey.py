from flask import Flask, render_template, request, redirect 

app = Flask(__name__)
            
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def process_form():
    print(request.form)
    users_index = request.form['username']
    location_index = request.form['location']
    language_index = request.form['language']
    comment_index = request.form['comment']

    return render_template("info.html", name= users_index, loc = location_index, lang = language_index,com = comment_index)

if __name__ == "__main__":
    app.run(debug=True)
