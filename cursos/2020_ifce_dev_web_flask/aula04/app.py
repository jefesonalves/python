from flask import Flask, request, redirect
from flask import render_template

app = Flask(__name__)
lista = ["antonio", "maria"]

@app.route("/")
def inicio():
    return render_template("inicio.html", nomes=lista)

@app.route("/novo")
def novo():
    return render_template("novo.html")

@app.route("/criar", methods=["POST",])
def criar():
    nome = request.form["nome"]
    lista.append(nome)
    return redirect("/")

app.run(debug=True)