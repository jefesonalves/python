from flask import Flask, request, redirect, flash, session, url_for
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "q1w2e34rwer23"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    nome = db.Column("nome", db.String(100))

    def __init__(self, nome):
        self.nome = nome


@app.route("/")
def inicio():
    return render_template("inicio.html", usuarios=users.query.all())

@app.route("/novo")
def novo():
    if "usuario" not in session or session["usuario"] == None:
        return redirect(url_for("login"))
    else:
        return render_template("novo.html")        
    
@app.route("/criar", methods=["POST",])
def criar():
    nome = request.form["nome"]
    usuario = users(nome)
    db.session.add(usuario)
    db.session.commit()
    return redirect(url_for("inicio"))

@app.route("/editar/<id>")
def editar(id):
    usuario = users.query.filter_by(_id=id).first()
    return render_template("editar.html", nome=usuario.nome, id=usuario._id)

@app.route("/atualizar", methods=["POST",])
def atualizar():
    nome = request.form["nome"]
    id = int(request.form["id"])
    usuario = users.query.filter_by(_id=id).first()
    usuario.nome = nome #usuario 2
    db.session.commit()    
    return redirect(url_for("inicio"))

@app.route("/deletar/<id>")
def deletar(id):
    id = int(id)
    usuario = users.query.filter_by(_id=id).first() #user7
    db.session.delete(usuario)
    db.session.commit()
    return redirect(url_for("inicio"))

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/autenticar", methods=["POST",])
def autenticar():
    nome_usuario = request.form["nome"]
    senha = request.form["senha"]    
    if nome_usuario == "teste" and senha == "1234":
        flash("Usuário logado com sucesso!")
        session["usuario"] = nome_usuario
        return redirect(url_for("inicio"))
    else:
        flash("Usuário ou senha inválido!")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
        session["usuario"] = None
        return redirect(url_for("login"))

db.create_all()
app.run(debug=True)