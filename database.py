import sqlite3

class Data_base():

    def __init__ (self, name = "banco_de_dados.db") -> None:
        self.name = name
        self.connection = name

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.name)
        except:
            print("Não conseguiu abrir o banco de dados.")


    def close_connection(self):
        try:
            self.connection.close()

        except:
            print("Não conseguiu fechar o banco de dados.")


    def cadastrarUsuario(self):
        