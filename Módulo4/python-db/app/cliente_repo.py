import sqlite3
from database import Database
from conn import Connection

class ClienteRepository:
    def __init__(self, database: Database):
        self.db = database
    
    def listar_todos(self):
        try:
            with Connection() as (conn, cursor):
                cursor.execute("SELECT * FROM cliente")
                return cursor.fetchall()
        except sqlite3.Error as e:
            print("Erro ao buscar clientes:", e)
            return []
        
    def criar(self, nome, email, telefone):
        sql = """
        INSERT INTO cliente (nome, email, telefone)
        VALUES (?, ?, ?)
        """
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, (nome, email, telefone))
            conn.commit()
            novo_id = cursor.lastrowid
            return novo_id
        except sqlite3.Error as e:
            print("Erro ao criar cliente, verifique os dados.", e)
            return []
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals():
                conn.close()
            

    def atualizar_telefone(self, id, novo_telefone):
        sql = "UPDATE cliente SET telefone = ? WHERE id = ?"
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (novo_telefone, id))
        conn.commit()
        linhas = cursor.rowcount  # quantas linhas foram afetadas
        cursor.close()
        conn.close()
        return linhas

    def buscar_por_email(self, email):
        sql = "SELECT 1 FROM cliente WHERE email = ?"
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, (email,))
            resultado = cursor.fetchone()
            return resultado is not None
        
        except sqlite3.Error as e:
            print("Erro ao buscar clientes:", e)
            return []
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals():
                conn.close()
            