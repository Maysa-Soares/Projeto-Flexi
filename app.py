from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

@app.route('/')
def homepage():
    return "Rede social de fotos - Flexi"

if __name__ == '__main__':
    app.run(debug=True)