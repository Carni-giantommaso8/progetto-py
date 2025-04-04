from flask import Flask, render_template

app = Flask(__name__)

lista = ["luca","pizza","motore","focaccia","telefono"]

@app.route('/')
def aggiungi():
    elemento = re


def home():

    return render_template("index.html" , lista = lista) 


if __name__ == '__main__':
    app.run(debug=True)
