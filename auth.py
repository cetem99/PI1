from flask import *
from flask import render_template, request, Flask
from DAO import *
import hashlib


auth = Blueprint("auth", __name__, template_folder="templates")
app = Flask(__name__)


@auth.route("/login")
def login():
    return render_template("login.html")


@auth.route("/login", methods=["POST"])
def login_post():
    email = request.form.get("email")
    senha = hashlib.sha1(request.form.get("senha").encode("utf-8")).hexdigest()

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
