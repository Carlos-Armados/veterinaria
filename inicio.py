from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("veterinaria-1.html")

@app.route('/animales normales')
def contacto():
    return render_template("animales normales.html")

@app.route('/Ballenas')
def contacto():
    return render_template("Ballenas.html")

@app.route('/preistoricos')
def contacto():
    return render_template("preistoricos.html")

@app.route('/mitoanimal')
def contacto():
    return render_template("mitoanimal.html")

