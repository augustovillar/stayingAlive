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

    def cadastrar_usuario(self, nome):

        try:
            cursor = self.connection.cursor()
            cursor.execute(f"""
                            INSERT OR IGNORE INTO Usuarios values(NULL, '{nome}')
                          """)
            self.connection.commit()

            return "OK"
        except Exception as e:
            print(e)
            return "DEU ERRO!"

    def criarJogada(self, id_1, id_2, id_ganhador, pontos1, pontos2, nAbaixando, nDancando, nParadas):

        try:
            cursor = self.connection.cursor()
            cursor.execute(f"""
                            INSERT OR IGNORE INTO Jogos values(NULL, {id_1}, {id_2}, {id_ganhador}, {pontos1}, {pontos2}, {nAbaixando}, {nDancando}, {nParadas})
                          """)
            self.connection.commit()

            return "OK"
        except Exception as e:
            print(e)
            return "DEU ERRO!"

    def procura_historico_jogador(self, nome):
        cursor = self.connection.cursor()

        #primeiro descobre o id do jogador pelo nome
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"SELECT ID_USUARIO FROM Usuarios WHERE NOME = '{nome}'")
            jogador_id = cursor.fetchall()
        except Exception as e:
            print(e)
            return "DEU ERRO!"

        #busca informações do jogador
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"SELECT * FROM Jogos WHERE ID_JOGADOR1 = {jogador_id} OR ID_JOGADOR2 = {jogador_id}")
            return cursor.fetchall()
        except Exception as e:
            print(e)
            return "DEU ERRO!"

    def verifica_usuario(self, nome):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"SELECT ID_USUARIO FROM Usuarios WHERE NOME = '{nome}'")
            jogador_id = cursor.fetchall()
            return jogador_id
        except Exception as e:
            print(e)
            return "DEU ERRO!"

    # def procura_jogador_id(self, nome):

    #     try:
    #         cursor = self.connection.cursor()
    #         cursor.execute(f"SELECT ID_USUARIO FROM Usuarios WHERE NOME = '{nome}'")
    #         return cursor.fetchall()
    #     except Exception as e:
    #         print(e)
    #         return "DEU ERRO!"




    # def criar_tabela_Jogo(self):
    #     cursor = self.connection.cursor()

    #     cursor.execute("""

    #                     CREATE TABLE "Jogos" (
    #                     "ID_JOGO"	INTEGER NOT NULL,
    #                     "ID_JOGADOR1"	INTEGER NOT NULL,
    #                     "ID_JOGADOR2"	INTEGER NOT NULL,
    #                     "PONTOS1"	INTEGER,
    #                     "PONTOS2"	INTEGER,
    #                     PRIMARY KEY("ID_JOGO" AUTOINCREMENT),
    #                     FOREIGN KEY("ID_JOGADOR2") REFERENCES "Usuarios"("ID_USUARIO"),
    #                     FOREIGN KEY("ID_JOGADOR1") REFERENCES "Usuarios"("ID_USUARIO")
    #                 );
    #                     """)


    # def criar_tabela_Usuario(self):
    #     cursor = self.connection.cursor()

    #     cursor.execute("""

    #                     CREATE TABLE IF NOT EXISTS "Usuarios" (
    #                     "ID_USUARIO"	INTEGER NOT NULL,
    #                     "NOME"	TEXT NOT NULL UNIQUE,
    #                     PRIMARY KEY("ID_USUARIO" AUTOINCREMENT)
    #                     );
    #                     """)

    #     self.connection.commit()
