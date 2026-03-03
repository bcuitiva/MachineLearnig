from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Flask"

@app.route('/FirstPage')
def firstPage():
    return render_template('index.html')

@app.route('/CasoUso')
def casoUso():
    return render_template('casoUso.html')

@app.route('/UseCase')
def UseCase():
    return render_template('UseCase.html')