from flask import Flask,render_template,request
import datetime

app = Flask(__name__)

entries=[]
@app.route("/", methods=["POST","GET"])
def index():
    if request.method=="POST":
        entry_content=request.form.get("entry-f")
        formated_date=datetime.datetime.today().strftime("%y-%m-%d")
        entries.append((entry_content,formated_date))
    entries_with_date = [(entry[0],entry[1],
                          datetime.datetime.strptime(entry[1],"%y-%m-%d").strftime("%b %d")
                          )for entry in entries
                          ]
    return render_template("index.html", entries=entries_with_date)

