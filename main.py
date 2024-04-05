from flask import *
from auth import auth
from DAO import DAO
from datetime import date
from imagens_connection import insert_image
import openpyxl
import os

app = Flask(__name__)
app.register_blueprint(auth)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

def allowed_file(filename):
    UPLOAD_FOLDER = 'ocorrencias'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'webp'}
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/home")
def home():
    if "loggedin" in session and session["loggedin"] is True:
        if session["pessoa_permissao"]:
            exportar_excel = '<li><a href="/exportar_excel">Exportar Excel</a></li>'
            return render_template("Templatedic.html", nome=session["nome"].split()[0], execel_export = exportar_excel)
        else:
            exportar_excel = '<li><a href="/exportar_excel"></a></li>'
            return render_template("Templatedic.html", nome=session["nome"].split()[0], execel_export = exportar_excel)
    else:
        flash("Logue para acessar esta página.")
        return redirect(url_for("auth.login"))


@app.route("/")
def index():
    return render_template("index.html")

#rotas de erro
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html')

'''@app.errorhandler(Exception)
def internal_server_error(error):
    return render_template('500_error.html')'''



if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)