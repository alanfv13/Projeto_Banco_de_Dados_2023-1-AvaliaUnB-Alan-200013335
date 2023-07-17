# Projeto_Banco_de_Dados_2023-1-AvaliaUnB-Alan-200013335
Projeto de Banco de Dados UnB


Seja bem vindo ao meu projeto de banco de dados
Ele foi feito com MySQL e Flask pra o back e front

Vamos configura o seu ambiente para que ele rode tranquilamente 

Primeiramente: 
  Para criação do banco de dados ultilize o arquivo avaliaunb.db que se localiza na pasta Scripts
  (Nele se encontra o banco de dados, com suas tabelas relacionadas, com uma view, e os inserts nas tabelas)

Logo após:
  
  1 -Verifique se tem python instalado na sua máquina
  
  2 - Abra o terminal no diretorio do programa e crie uma venv. (Ex Windows: python -m venv venv)

  3 - Agora ative a venv. (Ex Windows: .\venv\Scripts\Activate.ps1)

  4 - Instale o Flask:
    'pip install flask'

  5 - Instale também:
    'pip install mysql.connector', 'pip install pip install mysql-connector-python'

  6 - Vá até UserModel.py na pasta models e altere o db_config
    db_config = {
    'host': 'localhost',
    'user': 'seu usuario', 
    'password': 'Sua senha',
    'database': 'avaliaunb',
    'port': 3306
    }

  7 - No terminal rode o comando
    'flask run'

  Pronto estará funcionando o projeto!

  

