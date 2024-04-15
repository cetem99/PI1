from flask import render_template, request, Flask, Blueprint, flash, url_for, redirect, session
from DAO import CheckCadastro, CheckLogin, selectFromWhere, insertCadastro
from hashlib import sha256


auth = Blueprint("auth", __name__, template_folder="templates")
app = Flask(__name__)


@auth.route("/login")
def login():
    return render_template("login.html")


@auth.route("/login", methods=["POST"])
def login_post():
    email = request.form.get("email")
    senha = sha256(request.form.get("senha").encode("utf-8")).hexdigest()

    count = CheckLogin(email, senha)

    # Se não logar...
    if count == 0:
        flash("Senha e/ou Email incorretos")
        return redirect(url_for("auth.login"))

    # se logar...
    session["loggedin"] = True
    session["id"] = selectFromWhere("tb_usuario", "user_email", email, "user_id")
    session["nome"] = selectFromWhere("tb_usuario", "user_email", email, "user_name")
    session["pessoa_permissao"] = selectFromWhere(
        "tb_usuario", "user_email", email, "TODO"
    )
    session["email"] = email

    return redirect(url_for("home"))


@auth.route("/cadastro")
def cadastro():
    return render_template("Cadastro.html")

@auth.route("/cadastro", methods = ["POST"])
def registro_post():
    email = request.form.get("email")
    senha = request.form.get("senha")
    nome1 = request.form.get("nome1")
    nome2 = request.form.get("nome2")
    cpf = request.form.get("cpf")

    checkEmail = CheckCadastro("user_email", email)
    checkCPF = CheckCadastro("user_cpf", cpf)

    if checkEmail >= 1:
        flash("Email já cadastrado!")
        return redirect(url_for("auth.cadastro"))
    elif checkCPF >= 1:
        flash("CPF já cadastrado")
        return redirect(url_for("auth.cadastro"))
    elif(
        not email
        or not senha
        or not nome1
        or not nome2
        or not cpf
        
    ):
        flash("Preencha o formulário todo!")
        return redirect(url_for("cadastro"))
    
    else:
        senhaHash = sha256(senha.encode("utf-8")).hexdigest()
        insertCadastro(email, senhaHash, nome1, nome2, cpf)
        flash("Cadastrado com sucesso!")
        return redirect(url_for("auth.login"))
        

