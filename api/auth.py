from flask import render_template, request, Flask, Blueprint, flash, url_for, redirect, session
from DAO import CheckCadastro, CheckLogin, selectFromWhere, insertCadastro
from hashlib import sha256
from envio_email import gerar_codigo, enviar_email

codigos_de_verificacao = {}

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
        # fazer a checagem por código de verificação
        codigo_verificacao = gerar_codigo()
        codigos_de_verificacao[email] = codigo_verificacao
        enviar_email(nome1, codigo_verificacao, email)
        
        senhaHash = sha256(senha.encode("utf-8")).hexdigest()
        insertCadastro(email, senhaHash, nome1, nome2, cpf)
        flash("Cadastrado com sucesso!")
        return redirect(url_for("auth.login"))        

@auth.route("/verificar_email")
def cadastro():
    return render_template("verificar_email.html")

@auth.route("/verificar_email", methods=["POST"])
def verificar_email(email):
    
    if request.method == "POST":
        codigo_inserido = request.form.get("codigo")  # Obtém o código de verificação inserido pelo usuário

        
        # Verifica se o código inserido pelo usuário corresponde ao código enviado por e-mail
        codigo_gerado = codigos_de_verificacao.get(email)
        if codigo_gerado and codigo_inserido == codigo_gerado:
            # Se o código estiver correto, redireciona o usuário para a página de login
            flash("E-mail verificado com sucesso! Faça login para continuar.")
            return 
        else:
            # Se o código estiver incorreto, exibe uma mensagem de erro e redireciona o usuário de volta para a página de verificação
            flash("Código de verificação incorreto. Por favor, tente novamente.")
            return redirect(url_for("auth.verificar_email"))