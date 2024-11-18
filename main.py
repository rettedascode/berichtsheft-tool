from flask import Flask, request, send_from_directory, jsonify, render_template, url_for, redirect, flash
from pathlib import Path
from flask_wtf import CSRFProtect

from src.forms.LoginForm import LoginForm

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
csrf = CSRFProtect(app)
csrf._csrf_disable = True

# Directory containing HTML files
html_dir = Path(__file__).parent


# Routes for each HTML file
@app.route("/azubi-index")
def get_azubi_index():
    return render_template("azubi-index.html")
    # return send_from_directory(html_dir, "azubi-index.html")


@app.route("/")
def get_index():
    return send_from_directory(html_dir, "index.html")


@app.route("/login")
def get_login():
    form = LoginForm()
    return render_template('login.html', form=form, errorValues=[])
    # return send_from_directory(html_dir, "login.html")


@app.route("/nachweis-signen")
def get_nachweis_signen():
    return render_template("nachweis-signen.html")
    #return send_from_directory(html_dir, "nachweis-signen.html")


# API endpoint for login
@app.route("/api/login", methods=["POST"])
def api_login():
    username = request.form.get("username")
    password = request.form.get("password")
    # Simulate authentication logic (for demonstration purposes)
    form = LoginForm()
    # form.populate_obj({'login': username, 'password': password}.)

    if form.validate():
        if username == "admin" and password == "password":
            flash('You were successfully logged in as Admin')
        else:
            flash('You were successfully logged in')

        return redirect(url_for('get_azubi_index'))

    else:
        errorValues = [
            form.data['login'],
            form.data['password'],
        ]
        flash(
                'Die Eingabe ist fehlerhaft. Bitte korrigieren.',
                'danger')
        return render_template('login.html', form=form, errorValues=errorValues)
        #return jsonify({"message": "Invalid credentials"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
