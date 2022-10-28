from flask import Flask, redirect, render_template
import string
import secrets

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('testes.html')


@app.errorhandler(404)
def not_found(e):
    return redirect('/index')


@app.route('/gerador')
def gerador():
    comprimento = 14
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(password_characters) for i in range(comprimento))
    return render_template('flexbox.html',senha = password)



if __name__ == '__main__':
    app.run(debug = True)