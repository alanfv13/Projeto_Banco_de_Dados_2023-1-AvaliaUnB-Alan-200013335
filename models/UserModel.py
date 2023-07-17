import mysql.connector
from mysql.connector import Error
from functools import wraps

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'avaliaunb',
    'port': 3306
}


def obter_ultima_matricula():
    try:
        connection = mysql.connector.connect(**db_config)
        query = "SELECT MAX(matricula) FROM Estudantes"
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        return result[0] if result[0] is not None else 0
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")


def cadastrar_estudante(matricula, nome, email, curso, senha, administrador, imagem):
    try:
        connection = mysql.connector.connect(**db_config)
        query = "INSERT INTO Estudantes (matricula, nome, email, curso, senha, administrador, imagem) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        imagem_bytes = imagem.read() if imagem else None
        values = (matricula, nome, email, curso, senha, administrador, imagem_bytes)
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()
        print("Estudante cadastrado com sucesso!")
        print(f"Matrícula do estudante: {matricula}")
        return True
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return False


def verificar_credenciais(email, senha):
    try:
        # Conecta ao banco de dados
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Executa a consulta SQL para obter as informações do estudante
        query = "SELECT admin FROM estudantes WHERE email = %s AND senha = %s"
        cursor.execute(query, (email, senha))
        result = cursor.fetchone()

        # Fecha a conexão com o banco de dados
        cursor.close()
        conn.close()

        # Verifica se as credenciais estão corretas e retorna True ou False
        if result and result[0] == 1:
            return True  # Estudante é um administrador
        else:
            return False  # Estudante não é um administrador

    except mysql.connector.Error as error:
        print("Erro ao conectar ao banco de dados:", error)
        return False


def verificar_credenciais(email, senha):
    try:
        # Conecta ao banco de dados
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Executa a consulta SQL para obter as informações do estudante
        query = "SELECT * FROM Estudantes WHERE email = %s AND senha = %s"
        cursor.execute(query, (email, senha))
        result = cursor.fetchone()

        # Fecha a conexão com o banco de dados
        cursor.close()
        conn.close()

        # Verifica se as credenciais estão corretas e retorna True ou False
        return result

    except mysql.connector.Error as error:
        print("Erro ao conectar ao banco de dados:", error)
        return False


def deletar_user(user_id):
    try:
        # Conecta ao banco de dados
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Executa a consulta SQL para excluir a conta do usuário
        query = "DELETE FROM Estudantes WHERE matricula = %s"
        cursor.execute(query, (user_id,))
        conn.commit()

        # Fecha a conexão com o banco de dados
        cursor.close()
        conn.close()

        # Verifica se as credenciais estão corretas e retorna True ou False
        return True

    except mysql.connector.Error as error:
        print("Erro ao conectar ao banco de dados:", error)
        return False


def modificar_dados_estudante(matricula, nome, email, curso):
    try:
        connection = mysql.connector.connect(**db_config)
        query = "UPDATE Estudantes SET nome = %s, email = %s, curso = %s WHERE matricula = %s"
        values = (nome, email, curso, matricula)
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()
        return True
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return False


def obter_dados_estudante(matricula):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Executa a consulta SQL para obter a matrícula do usuário pelo email
        query = "SELECT matricula FROM Estudantes WHERE matricula = %s"
        cursor.execute(query, (matricula,))
        result = cursor.fetchone()

        # Fecha a conexão com o banco de dados
        cursor.close()
        conn.close()

        # Retorna a matrícula se encontrada, caso contrário retorna None
        if result:
            return result[0]
        else:
            return None
    except Error as error:
        print(f"Erro ao conectar ao MySQL: {error}")
        return None
