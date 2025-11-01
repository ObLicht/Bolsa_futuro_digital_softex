from app.db import Database

class ClienteRepository:
    def __init__(self, db: Database):
        self.db = db

    def listar_todos(self):
        sql = "SELECT id, nome, email, telefone, criado_em FROM cliente ORDER BY criado_em DESC"
        conn = self.db.get_connection()
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(sql)
            resultados = cursor.fetchall()
            cursor.close()
            return resultados
        finally:
            conn.close()