import tkinter as tk
from tkinter import ttk
import bd_manipulador


class EuricoRefeicoes:
    def __init__(self):
        self.__banco = bd_manipulador.Banco()

        self.__janela = tk.Tk()
        self.__janela.title("Cadastro Ingredientes")
        self.__dimensoes = int(self.__janela.winfo_screenwidth() * 0.2), int(self.__janela.winfo_screenheight() * 0.25)
        self.__janela.geometry(f"{self.__dimensoes[0]}x{self.__dimensoes[1]}+{int(self.__dimensoes[0] * 2)}+{int(self.__dimensoes[1])}")
        self.__janela.resizable(False, False)
        self.__janela.config(bg="gray25")

    def cadastro_ingrediente(self):
        self.__janela.grid_columnconfigure(0, weight=1)
        self.__janela.grid_columnconfigure(1, weight=2)
        self.__janela.rowconfigure(0, weight=2)
        self.__janela.rowconfigure(1, weight=2)
        self.__janela.rowconfigure(2, weight=2)
        self.__janela.rowconfigure(3, weight=2)
        self.__janela.rowconfigure(4, weight=2)
        self.__janela.rowconfigure(5, weight=1)

        fonte = "garuda", self.__dimensoes[0] * self.__dimensoes[1] // 7000
        wid = self.__dimensoes[0] // 18

        lb = ttk.Label(self.__janela, text="Nome:", background="gray25", foreground="snow")
        lb["font"] = fonte
        lb.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        ent1 = ttk.Entry(self.__janela, width=wid)
        ent1["font"] = fonte
        ent1.grid(row=0, column=1, sticky=tk.W)

        lb = ttk.Label(self.__janela, text="Calorias:", background="gray25", foreground="snow")
        lb["font"] = fonte
        lb.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        ent2 = ttk.Entry(self.__janela, width=wid)
        ent2["font"] = fonte
        ent2.grid(row=1, column=1, sticky=tk.W)

        lb = ttk.Label(self.__janela, text="Proteinas:", background="gray25", foreground="snow")
        lb["font"] = fonte
        lb.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        ent3 = ttk.Entry(self.__janela, width=wid)
        ent3["font"] = fonte
        ent3.grid(row=2, column=1, sticky=tk.W)

        lb = ttk.Label(self.__janela, text="Carboidratos:", background="gray25", foreground="snow")
        lb["font"] = fonte
        lb.grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
        ent4 = ttk.Entry(self.__janela, width=wid)
        ent4["font"] = fonte
        ent4.grid(row=3, column=1, sticky=tk.W)

        lb = ttk.Label(self.__janela, text="Gorduras:", background="gray25", foreground="snow")
        lb["font"] = fonte
        lb.grid(row=4, column=0, padx=5, pady=5, sticky=tk.E)
        ent5 = ttk.Entry(self.__janela, width=wid)
        ent5["font"] = fonte
        ent5.grid(row=4, column=1, sticky=tk.W)

        def cadastrar():
            cor = "green"
            try:
                self.__banco.add_ingrediente(ent1.get(), int(ent2.get()), float(ent3.get()), float(ent4.get()), float(ent5.get()))
                ent1.delete(0, tk.END)
                ent2.delete(0, tk.END)
                ent3.delete(0, tk.END)
                ent4.delete(0, tk.END)
                ent5.delete(0, tk.END)
                print(self.__banco)
                self.__banco.salvar()
            except Exception as err:
                print(err)
                cor = "red"

            lb = ttk.Label(self.__janela, text="*", font=16, background="gray25", foreground=cor)
            lb.grid(row=5, column=1)
            self.__janela.after(1000, lb.destroy)

        bt = ttk.Button(self.__janela, text="CADASTRAR", command=cadastrar)
        bt.grid(row=5, column=1, sticky=tk.E, padx=10, pady=5)
        self.__janela.mainloop()


if __name__ == "__main__":
    EuricoRefeicoes().cadastro_ingrediente()
