from flask import Flask, request, send_from_directory, jsonify, render_template
from pathlib import Path

app = Flask(__name__)

# Directory containing HTML files
html_dir = Path(__file__).parent


# Routes for each HTML file
@app.route("/azubi-index")
def get_azubi_index():
    return send_from_directory(html_dir, "azubi-index.html")


@app.route("/")
def get_index():
    return send_from_directory(html_dir, "index.html")


@app.route("/login")
def get_login():
    return send_from_directory(html_dir, "login.html")


@app.route("/nachweis-signen")
def get_nachweis_signen():
    return send_from_directory(html_dir, "nachweis-signen.html")


# API endpoint for login
@app.route("/api/login", methods=["POST"])
def api_login():
    username = request.form.get("username")
    password = request.form.get("password")
    # Simulate authentication logic (for demonstration purposes)
    if username == "admin" and password == "password":
        return jsonify({"message": "Login successful", "redirect": "/azubi-index"})
    return jsonify({"message": "Invalid credentials"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
