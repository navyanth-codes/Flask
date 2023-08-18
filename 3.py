from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index1():
    return  render_template('index.html')

@app.route("/about")
def about1():
    name="navyanth"
    return render_template('about.html',name2=name)

@app.route("/bootstrap")
def bootstarp():
    return render_template('boot.html')    #using bootstrap in flask

app.run(debug=True)