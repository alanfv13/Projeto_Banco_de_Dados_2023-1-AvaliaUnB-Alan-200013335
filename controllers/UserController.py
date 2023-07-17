from flask import session, flash, redirect, url_for

from models.UserModel import *


def create(request):
    try:
        matricula = request.form.get('matricula')
        nome = request.form.get('nome')
        email = request.form.get('email')
        curso = request.form.get('curso')
        senha = request.form.get('senha')
        administrador = False
        imagem = request.files.get('imagem')

        if not nome.strip():
            raise ValueError('Nome não fornecido')
        if not email.strip():
            raise ValueError('Email não fornecido')
        if not curso.strip():
            raise ValueError('Curso não fornecido')
        if not senha.strip():
            raise ValueError('Senha não fornecida')
        if matricula is None:
            raise ValueError('Matrícula não fornecida')
        if imagem and imagem.filename == '':
            raise ValueError('Nenhum arquivo selecionado')

        response = cadastrar_estudante(matricula, nome, email, curso, senha, administrador, imagem)
        return response
    except KeyError:
        return f'Erro ao cadastrar o estudante: Campos obrigatórios não fornecidos. Dados recebidos: {str(request.form)}', 400

    except ValueError as e:
        return f'Erro ao cadastrar o estudante: {str(e)}. Dados recebidos: {str(request.form)}', 400

    except Exception as e:
        return f'Erro ao cadastrar o estudante: {str(e)}. Dados recebidos: {str(request.form)}', 500


def validate(request):
    email = request.form.get('email')
    senha = request.form.get('senha')

    response = verificar_credenciais(email, senha)

    if response:
        # Credenciais corretas, armazena as informações do usuário na sessão
        session['logged_in'] = True
        session['user_id'] = response[0]
        session['user_email'] = response[2]
        return True
    else:
        # Credenciais incorretas
        return False


def excluir_user():
    try:
        # Obtém o ID do usuário da sessão
        user_id = session['user_id']
        response = deletar_user(user_id)

        # Limpa a sessão e redireciona para a página de login
        session.clear()
        flash('Sua conta foi excluída com sucesso.', 'success')
        return response

    except Error as error:
        flash('Erro ao excluir a conta. Por favor, tente novamente.', 'error')
        return False


def update_user(request, matricula):
    nome = request.form.get('nome')
    email = request.form.get('email')
    curso = request.form.get('curso')

    if modificar_dados_estudante(matricula, nome, email, curso):
        flash('Dados da conta modificados com sucesso!', 'success')
        return True
    else:
        flash('Erro ao modificar os dados da conta.', 'error')
        return False


def get_user(matricula):
    return obter_dados_estudante(matricula)


# Decorator para verificar se o usuário está logado
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Faça login para acessar esta página.', 'error')
            return redirect(url_for('login'))

    return decorated_function
