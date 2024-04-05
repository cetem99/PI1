from flask import *
from auth import auth

app = Flask(__name__)
app.register_blueprint(auth)

app.secret_key = "uhrq3ur23guyrh"


@app.route("/home")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
