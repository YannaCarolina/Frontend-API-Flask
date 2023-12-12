Para a configuração correta da API, é necessário configurar um banco de dados mysql mudando o: app.config['MYSQL_HOST'] = '127.0.0.1' -> deixar padrão se a configuração do host for a padrão app.config['MYSQL_PORT'] = 3308 -> mudar a porta para a porta disponível no banco de dados app.config['MYSQL_USER'] = 'root' -> criar o usuário root app.config['MYSQL_PASSWORD'] = 'root' -> com a senha root app.config['MYSQL_DB'] = 'produtos' -> criar uma database para os produtos. app.config['MYSQL_CURSORCLASS'] = 'DictCursor' -> manter padrão.

Utilizar o seguinte código no mysql: CREATE DATABASE produtos; USE produtos;

CREATE TABLE produtos(id INT PRIMARY KEY AUTO_INCREMENT, nome VARCHAR(250) NOT NULL, descricao LONGTEXT NOT NULL, estoque BOOL NOT NULL); SELECT * FROM produtos;

Após isso, fazer o download o projeto e instalar as dependências em uma virtual env: pip install Flask Flask-MySQLdb. Depois, só rodar e o aplicativo cairá no endpoint padrão, só realizar o cadastro.
