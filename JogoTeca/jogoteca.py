from flask import Flask, render_template, request

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

# Variáveis Global
jogo_01 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo_02 = Jogo('Skyrum', 'RPG', 'PC')
jogo_03 = Jogo('Crash', 'Ação', 'Playstation')
jogo_04 = Jogo('Final Fantasy VII', 'RPG', 'Playstation')
lista_de_jogos = [jogo_01, jogo_02, jogo_03, jogo_04]
        
app = Flask(__name__)

# Criando a rota principal
@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista_de_jogos)

# Criando uma nova rota
@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html', titulo='Cadastrar novo jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista_de_jogos.append(jogo)
    return render_template('lista.html', titulo='Jogos', jogos=lista_de_jogos)

if __name__ == '__main__':
    app.run(debug=True)