from flask import Flask, render_template

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console
        
app = Flask(__name__)

# Criando a rota principal
@app.route('/')
def inicio():
    jogo_01 = Jogo('Tetris', 'Puzzle', 'Atari')
    jogo_02 = Jogo('Skyrum', 'RPG', 'PC')
    jogo_03 = Jogo('Crash', 'Ação', 'Playstation')
    jogo_04 = Jogo('Final Fantasy VII', 'RPG', 'Playstation')
    lista_de_jogos = (jogo_01, jogo_02, jogo_03, jogo_04)
    return render_template('lista.html', titulo='Jogos', jogos=lista_de_jogos)

# Criando uma nova rota
@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html', titulo='Cadastrar novo jogo')

if __name__ == '__main__':
    app.run()