from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from funcs import macro_placer
from datetime import datetime


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///MacroMania.db"
db = SQLAlchemy(app)

class MacroHist(db.Model):
    sno = db.Column(db.Integer, primary_key = True )
    tag = db.Column(db.String(500), nullable = False )
    macro_tag = db.Column(db.String(500), nullable = False )
    date =  db.Column(db.DateTime, default = datetime.utcnow )

    def __repr__(self) -> str:
        return f"{self.sno} - {self.tag[0-10]}"
    
with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def home():  

    if request.method == "POST":

        user_tag = request.form["tag"]

        tag = macro_placer(user_tag)

        return render_template("home.html", final_tag = tag)
    
    else:
        return render_template("home.html")
    

@app.route("/history", methods=["GET","POST"])
def history():
    return render_template("history.html")


if __name__ == "__main__":

    app.run(debug=True)
