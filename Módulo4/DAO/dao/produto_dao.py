import sqlite3
from models.produto import Produto

class ProdutoDAO:
    def __init__(self, db_name='produtos.db'):
            self.db_name = db_name
            self._criar_tabela()

    def _criar_tabela(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS produto (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    item VACHAR NOT NULL
                )
            ''')

    def salvar(self, produto: Produto):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO produto (item) VALUES (?)',
                           (produto.item))
            conn.commit()

    def listar(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT item FROM produto')
            rows = cursor.fetchall()
            return [Produto(item) for item in rows]