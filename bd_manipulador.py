import sqlite3 as sq


class Banco:
    def __init__(self):
        self.__banco = sq.connect("bd_sistema.db")
        self.__cursor = self.__banco.cursor()

    def manual(self, comando):
        return self.__cursor.execute(comando)

    def salvar(self):
        self.__banco.commit()

    def add_ingrediente(self, nome, calorias: int, proteinas: float, carboidratos: float, gorduras: float):
        self.__cursor.execute(f"""INSERT INTO ingredientes (nome, calorias, proteinas, carboidratos, gorduras) 
        VALUES ('{nome}', {calorias}, {proteinas:.1f}, {carboidratos:.1f}, {gorduras:.1f})""")

    def del_ingrediente(self, nome):
        self.__cursor.execute(f"DELETE FROM ingredientes WHERE nome = '{nome}'")

    def get_ingrediente(self, nome):
        return self.__cursor.execute(f"SELECT * FROM ingredientes WHERE nome = {nome}")

    def close(self):
        self.__cursor.close()
        self.__banco.close()

    def __str__(self):
        self.__cursor.execute("SELECT * FROM ingredientes")
        aux = self.__cursor.fetchall()
        saida = ""
        for i in aux:
            saida += str(i) + "\n"
        return saida


if __name__ == "__main__":
    bd = Banco()

    while input("Prescione '-' para sair: ") != "-":
        try:
            print(bd.manual(input("Comando: ")).fetchone())
            print(bd)
            if input("Salvar (y/n)?") == "y":
                bd.salvar()
        except Exception as err:
            print(err)
