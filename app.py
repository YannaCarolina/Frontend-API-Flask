from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_PORT'] = 3308
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'produtos'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/cadastro', methods=['GET'])
def mostrar_formulario_cadastro():
    return render_template('cadastro.html')

@app.route('/cadastro', methods=['POST'])
def cadastrar_produto():
    nome = request.form['nome']
    descricao = request.form['descricao']
    estoque = request.form.get('estoque') == 'on'

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO produtos (nome, descricao, estoque) VALUES (%s, %s, %s)",
                (nome, descricao, estoque))
    mysql.connection.commit()
    cur.close()

    return redirect(url_for('cadastro_concluido'))

@app.route('/cadastro_concluido')
def cadastro_concluido():
    return render_template('cadastro_concluido.html')

@app.route('/listagem', methods=['GET'])
def listar_produtos():
    search_query = request.args.get('search', '')

    cur = mysql.connection.cursor()


    if not search_query:
        cur.execute("SELECT * FROM produtos")
    else:

        cur.execute("SELECT * FROM produtos WHERE id = %s OR nome LIKE %s",
                    (search_query, f'%{search_query}%'))

    produtos = cur.fetchall()
    cur.close()

    return render_template('listagem.html', produtos=produtos)

@app.route('/excluir/<int:produto_id>', methods=['GET'])
def confirmar_exclusao(produto_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM produtos WHERE id = %s", (produto_id,))
    produto = cur.fetchone()
    cur.close()
    return render_template('confirmar_exclusao.html', produto=produto)

@app.route('/excluir/<int:produto_id>/confirmar', methods=['POST'])
def excluir_produto(produto_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM produtos WHERE id = %s", (produto_id,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('listar_produtos'))

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)