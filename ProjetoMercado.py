import tkinter as tk
from tkinter import messagebox

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mercadinho do Zé")
        self.geometry("750x450")

        self.nome = ""
        self.contato = ""
        self.cpf = ""
        self.produtos = []
        self.forma_pagamento = ""

        self.create_widgets()

    def create_widgets(self):
        self.frame1 = tk.Frame(self)
        self.frame1.pack()

        self.label_space = tk.Label(self.frame1, text="")
        self.label_space.grid(row=0, column=0, pady=55)
        
        self.label_nome = tk.Label(self.frame1, text="Nome:")
        self.label_nome.grid(row=1, column=0)
        self.entry_nome = tk.Entry(self.frame1)
        self.entry_nome.grid(row=2, column=0)

        self.label_contato = tk.Label(self.frame1, text="Contato:")
        self.label_contato.grid(row=3, column=0)
        self.entry_contato = tk.Entry(self.frame1)
        self.entry_contato.grid(row=4, column=0)

        self.label_cpf = tk.Label(self.frame1, text="CPF:")
        self.label_cpf.grid(row=5, column=0)
        self.entry_cpf = tk.Entry(self.frame1)
        self.entry_cpf.grid(row=6, column=0)

        self.button_next1 = tk.Button(self.frame1, text="Próximo", command=self.next_screen1)
        self.button_next1.grid(row=7, columnspan=2)

    def next_screen1(self):
        self.nome = self.entry_nome.get()
        self.contato = self.entry_contato.get()
        self.cpf = self.entry_cpf.get()

        self.frame1.destroy()

        self.frame2 = tk.Frame(self)
        self.frame2.pack()

        self.label_nome_produto = tk.Label(self.frame2, text="\n\n\n\n\n\n\n\n\nNome do Produto:")
        self.label_nome_produto.grid(row=0, column=0)
        self.entry_nome_produto = tk.Entry(self.frame2)
        self.entry_nome_produto.grid(row=1, column=0)

        self.label_quantidade = tk.Label(self.frame2, text="Quantidade:")
        self.label_quantidade.grid(row=2, column=0)
        self.entry_quantidade = tk.Entry(self.frame2)
        self.entry_quantidade.grid(row=3, column=0)

        self.label_preco = tk.Label(self.frame2, text="Preço:")
        self.label_preco.grid(row=4, column=0)
        self.entry_preco = tk.Entry(self.frame2)
        self.entry_preco.grid(row=5, column=0)

        self.button_add_product = tk.Button(self.frame2, text="Adicionar Produto", command=self.add_product)
        self.button_add_product.grid(row=6, columnspan=2)

        self.button_next2 = tk.Button(self.frame2, text="Próximo", command=self.next_screen2)
        self.button_next2.grid(row=7, columnspan=2)

    def add_product(self):
        nome_produto = self.entry_nome_produto.get()
        quantidade = int(self.entry_quantidade.get())
        preco = float(self.entry_preco.get())

        self.produtos.append((nome_produto, quantidade, preco))

        self.entry_nome_produto.delete(0, tk.END)
        self.entry_quantidade.delete(0, tk.END)
        self.entry_preco.delete(0, tk.END)

    def next_screen2(self):
        self.frame2.destroy()

        self.frame3 = tk.Frame(self)
        self.frame3.pack()

        self.label_forma_pagamento = tk.Label(self.frame3, text="\n\n\n\n\n\n\n\n\nForma de Pagamento:")
        self.label_forma_pagamento.grid(row=1, column=0)

        self.var_pagamento = tk.StringVar()
        self.radio_credito = tk.Radiobutton(self.frame3, text="Crédito", variable=self.var_pagamento, value="Crédito")
        self.radio_credito.grid(row=2, column=0)
        self.radio_debito = tk.Radiobutton(self.frame3, text="Débito", variable=self.var_pagamento, value="Débito")
        self.radio_debito.grid(row=3, column=0)
        self.radio_pix = tk.Radiobutton(self.frame3, text="Pix", variable=self.var_pagamento, value="Pix")
        self.radio_pix.grid(row=4, column=0)
        self.radio_dinheiro = tk.Radiobutton(self.frame3, text="Dinheiro", variable=self.var_pagamento, value="Dinheiro")
        self.radio_dinheiro.grid(row=5, column=0)

        self.button_next3 = tk.Button(self.frame3, text="Próximo", command=self.next_screen3)
        self.button_next3.grid(row=6, columnspan=5)

    def next_screen3(self):
        self.forma_pagamento = self.var_pagamento.get()

        self.frame3.destroy()

        self.frame4 = tk.Frame(self)
        self.frame4.pack()
        
        self.label_nota_fiscal = tk.Label(self.frame4, text="\n\n\n\n\n\n\n\n\nNota Fiscal")
        self.label_nota_fiscal.pack()

        texto_nota = f"Nome: {self.nome}\nContato: {self.contato}\nCPF: {self.cpf}\n\nProdutos:\n"
        total = 0
        for produto in self.produtos:
            nome, quantidade, preco = produto
            total += quantidade * preco
            texto_nota += f"{nome} - Quantidade: {quantidade} - Preço: R${preco:.2f}\n"
        
        texto_nota += f"\nForma de Pagamento: {self.forma_pagamento}\n\nTotal: R${total:.2f}"
        
        self.label_nota = tk.Label(self.frame4, text=texto_nota)
        self.label_nota.pack()

if __name__ == "__main__":
    app = Application()
    app.mainloop()
