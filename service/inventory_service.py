import sqlite3

class InventoryService:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def get_all(self):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT rowid, * FROM inventory")
                rows = cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            print(f"Erro ao consultar a tabela inventory: {e}")
            return []
