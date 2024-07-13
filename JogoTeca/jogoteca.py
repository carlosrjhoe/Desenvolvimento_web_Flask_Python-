from flask import Flask, render_template

app = Flask(__name__)

# Criando a rota principal
@app.route('/')
def inicio():
    lista_de_jogos = ['Tetris', 'Skyrum', 'Crash', 'Final Fantasy VII', 'Final Fantasy VIII', 'Xenogers']
    return render_template('lista.html', titulo='Jogos', jogos=lista_de_jogos)

if __name__ == '__main__':
    app.run()