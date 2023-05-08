from flask import Flask


application = Flask(__name__)

from app.recognizer import view

application.register_blueprint(view.bp)

def main():
    application.run(host="0.0.0.0", port=5000, debug=True)
