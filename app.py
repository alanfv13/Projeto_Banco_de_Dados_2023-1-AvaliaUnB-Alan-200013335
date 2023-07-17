import secrets

from flask import Flask, render_template, request

from controllers.UserController import *

secret = secrets.token_urlsafe(32)

app = Flask(__name__)
app.secret_key = secret


# Rotas para Usuário
@app.route('/')
def index():  # put application's code here
    return render_template('index.html')

# Rotas para Usuário
@app.route('/indexlogado')
@login_required
def indexlogado():  # put application's code here
    return render_template('indexlogado.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        response = validate(request)

        if response:
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Credenciais incorretas. Tente novamente.', 'error')

    return render_template('user/login.html')


@app.route('/logout')
def logout():
    # Lógica para fazer o logout do usuário
    session.clear()  # Limpa a sessão
    flash('Você foi desconectado com sucesso!', 'success')
    return redirect(url_for('login'))


@app.route('/excluir_conta')
@login_required
def excluir_conta():
    if excluir_user():
        return redirect(url_for('login'))
    return redirect(url_for('dashboard'))


@app.route('/dashboard')
@login_required
def dashboard():
    # Acesso permitido apenas para usuários logados
    return render_template('dashboard.html')


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        criarUsuario = create(request)
        if criarUsuario:
            print('Estudante cadastrado com sucesso!', 200)
            return render_template('user/login.html')
        else:
            return render_template('user/cadastro.html')
    return render_template('user/cadastro.html')


@app.route('/editar_conta', methods=['GET', 'POST'])
@login_required
def editar_conta():
    matricula = session['user_id']

    if request.method == 'POST':
        if update_user(request, matricula):
            return redirect(url_for('dashboard'))

    estudante = get_user(matricula)
    return render_template('user/editar_conta.html', estudante=estudante)


if __name__ == '__main__':
    app.run()
