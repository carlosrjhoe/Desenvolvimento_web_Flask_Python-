from flask import Flask
from flask import flash
from flask import render_template
from flask import request
from flask import redirect
from flask import session
from flask import url_for


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha


# Variáveis Global

usuario_01 = Usuario('Carlos', 'carlosrjhoe', '12345')
usuario_02 = Usuario('Mayara', 'mayOiao', '12345')
usuario_03 = Usuario('Neto', 'carlosrneto', '12345')
usuarios = {
    usuario_01.nickname: usuario_01,
    usuario_02.nickname: usuario_02,
    usuario_03.nickname: usuario_03
}

jogo_01 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo_02 = Jogo('Skyrum', 'RPG', 'PC')
jogo_03 = Jogo('Crash', 'Ação', 'Playstation')
jogo_04 = Jogo('Final Fantasy VII', 'RPG', 'Playstation')
lista_de_jogos = [jogo_01, jogo_02, jogo_03, jogo_04]

app = Flask(__name__)
app.secret_key = 'Neto_Luna'

# Criando a rota principal

@app.route('/')
def index():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proxima=url_for('cadastrar')))
    else:
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
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash("logaut efetuado com sucesso!")
    return redirect(url_for('index'))


@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            session['usuario_logado'] = request.form['usuario']
            flash(f"Usuário {usuario.nickname} logado com sucesso!")
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Usuário não logado!')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
