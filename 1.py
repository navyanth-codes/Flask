from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/navyanth")
def hello():                                    #ila create chesi link lo /navyanth ani kodith edi run avudi lekapothe paidi run avudi
    return "<p>Hello, Navyanth bhai  !</p>"

app.run(debug=True)   #by using debug=True will automatically relodes the website