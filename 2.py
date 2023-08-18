from flask import Flask,render_template
# static -- folder (andaraki display avudi contents) ane dani manam mana lab exam lo uploads lo chustam ga  alanti interface lantidi mana question papers pete folder la untadi
# templates -- error chupistadi enduku ante avi confidentaial kabati

app = Flask(__name__)

@app.route("/")
def index1():
    return  render_template('index.html')

@app.route("/about")
def about1():
    name="navyanth"
    return render_template('about.html',name2=name)  # we define name2 in html file

app.run(debug=True)