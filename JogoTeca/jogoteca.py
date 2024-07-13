from flask import Flask, render_template

app = Flask(__name__)

# Criando a rota principal
@app.route('/')
def inicio():
    return render_template('lista.html')

if __name__ == '__main__':
    app.run()