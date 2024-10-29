import tkinter as tk 
from tkinter import ttk

class MarmitariaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Paty Comida Saudável - Controle de Pedidos")
        self.root.configure(bg='black')
        
        self.pedidos = []
        self.despesas = []

        # Cabeçalho
        label_header = tk.Label(root, text="Controle de Pedidos", fg='yellow', bg='black', font=('Helvetica', 18, 'bold'))
        label_header.pack(pady=10)

        # Frame dos detalhes do pedido
        frame = tk.Frame(root, bg='black')
        frame.pack(pady=10)

        # Configuração da fonte
        font_config = ('Helvetica', 14)

        # Nome do cliente
        self.label_nome = tk.Label(frame, text="Nome do Cliente:", fg='yellow', bg='black', font=font_config)
        self.label_nome.grid(row=0, column=0, sticky='e', padx=5)
        self.entry_nome = tk.Entry(frame, font=font_config)
        self.entry_nome.grid(row=0, column=1, padx=5)

        # Kit escolhido
        self.label_kit = tk.Label(frame, text="Kit Escolhido:", fg='yellow', bg='black', font=font_config)
        self.label_kit.grid(row=0, column=2, sticky='e', padx=5)
        self.entry_kit = tk.Entry(frame, font=font_config)
        self.entry_kit.grid(row=0, column=3, padx=5)

        # Quantidade de marmitas
        self.label_quantidade = tk.Label(frame, text="Quantidade de Marmitas:", fg='yellow', bg='black', font=font_config)
        self.label_quantidade.grid(row=1, column=0, sticky='e', padx=5)
        self.entry_quantidade = tk.Entry(frame, font=font_config)
        self.entry_quantidade.grid(row=1, column=1, padx=5)

        # Valor do kit
        self.label_valor_kit = tk.Label(frame, text="Valor do Kit:", fg='yellow', bg='black', font=font_config)
        self.label_valor_kit.grid(row=1, column=2, sticky='e', padx=5)
        self.entry_valor_kit = tk.Entry(frame, font=font_config)
        self.entry_valor_kit.grid(row=1, column=3, padx=5)

        # Valor do frete
        self.label_frete = tk.Label(frame, text="Valor do Frete:", fg='yellow', bg='black', font=font_config)
        self.label_frete.grid(row=2, column=0, sticky='e', padx=5)
        self.entry_frete = tk.Entry(frame, font=font_config)
        self.entry_frete.grid(row=2, column=1, padx=5)

        # Valor pago
        self.label_valor_pago = tk.Label(frame, text="Valor Pago:", fg='yellow', bg='black', font=font_config)
        self.label_valor_pago.grid(row=2, column=2, sticky='e', padx=5)
        self.entry_valor_pago = tk.Entry(frame, font=font_config)
        self.entry_valor_pago.grid(row=2, column=3, padx=5)

        # Forma de pagamento
        self.label_pagamento = tk.Label(frame, text="Forma de Pagamento:", fg='yellow', bg='black', font=font_config)
        self.label_pagamento.grid(row=3, column=0, sticky='e', padx=5)
        self.entry_pagamento = tk.Entry(frame, font=font_config)
        self.entry_pagamento.grid(row=3, column=1, padx=5)

        # Valor que falta ser pago
        self.label_valor_faltante = tk.Label(frame, text="Valor Faltante:", fg='yellow', bg='black', font=font_config)
        self.label_valor_faltante.grid(row=3, column=2, sticky='e', padx=5)
        self.entry_valor_faltante = tk.Entry(frame, font=font_config)
        self.entry_valor_faltante.grid(row=3, column=3, padx=5)

        # Botões
        self.botao_salvar = tk.Button(root, text="Salvar Pedido", command=self.salvar_pedido, bg='yellow', fg='black', font=font_config)
        self.botao_salvar.pack(pady=5)

        self.botao_limpar = tk.Button(root, text="Limpar", command=self.limpar_campos, bg='yellow', fg='black', font=font_config)
        self.botao_limpar.pack(pady=5)

        self.botao_consultar = tk.Button(root, text="Consultar Pedidos", command=self.consultar_pedidos, bg='yellow', fg='black', font=font_config)
        self.botao_consultar.pack(pady=5)

        # Tabela de despesas
        self.frame_despesas = tk.Frame(root, bg='black')
        self.frame_despesas.pack(pady=10)

        self.label_despesas = tk.Label(self.frame_despesas, text="Despesas", fg='yellow', bg='black', font=('Helvetica', 18, 'bold'))
        self.label_despesas.grid(row=0, column=0, columnspan=2, pady=10)

        self.tree_despesas = ttk.Treeview(self.frame_despesas, columns=("Descrição", "Valor"), show='headings')
        self.tree_despesas.heading("Descrição", text="Descrição")
        self.tree_despesas.heading("Valor", text="Valor")
        self.tree_despesas.grid(row=1, column=0, columnspan=2)

        self.entry_descricao = tk.Entry(self.frame_despesas, font=font_config)
        self.entry_descricao.grid(row=2, column=0, padx=5, pady=5)
        self.entry_valor = tk.Entry(self.frame_despesas, font=font_config)
        self.entry_valor.grid(row=2, column=1, padx=5, pady=5)

        self.botao_adicionar_despesa = tk.Button(self.frame_despesas, text="Adicionar Despesa", command=self.adicionar_despesa, bg='yellow', fg='black', font=font_config)
        self.botao_adicionar_despesa.grid(row=3, column=0, columnspan=2, pady=5)

        self.botao_total_despesas = tk.Button(self.frame_despesas, text="Total de Despesas", command=self.mostrar_total_despesas, bg='yellow', fg='black', font=font_config)
        self.botao_total_despesas.grid(row=4, column=0, columnspan=2, pady=5)

    def salvar_pedido(self):
        pedido = {
            'nome': self.entry_nome.get(),
            'kit': self.entry_kit.get(),
            'quantidade': self.entry_quantidade.get(),
            'valor_kit': self.entry_valor_kit.get(),
            'frete': self.entry_frete.get(),
            'valor_pago': self.entry_valor_pago.get(),
            'pagamento': self.entry_pagamento.get(),
            'valor_faltante': self.entry_valor_faltante.get(),
        }
        self.pedidos.append(pedido)
        print(f"Pedido salvo: {pedido}")
        self.limpar_campos()

    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_kit.delete(0, tk.END)
        self.entry_quantidade.delete(0, tk.END)
        self.entry_valor_kit.delete(0, tk.END)
        self.entry_frete.delete(0, tk.END)
        self.entry_valor_pago.delete(0, tk.END)
        self.entry_pagamento.delete(0, tk.END)
        self.entry_valor_faltante.delete(0, tk.END)

    def consultar_pedidos(self):
        janela_consulta = tk.Toplevel(self.root)
        janela_consulta.title("Pedidos Salvos")
        janela_consulta.configure(bg='black')
        
        tree = ttk.Treeview(janela_consulta, columns=("Nome", "Kit", "Quantidade", "Valor Kit", "Frete", "Valor Pago", "Pagamento", "Valor Faltante"), show='headings')
        tree.heading("Nome", text="Nome")
        tree.heading("Kit", text="Kit")
        tree.heading("Quantidade", text="Quantidade")
        tree.heading("Valor Kit", text="Valor Kit")
        tree.heading("Frete", text="Frete")
        tree.heading("Valor Pago", text="Valor Pago")
        tree.heading("Pagamento", text="Pagamento")
        tree.heading("Valor Faltante", text="Valor Faltante")
        tree.pack(fill=tk.BOTH, expand=True)

        for pedido in self.pedidos:
            tree.insert("", tk.END, values=(pedido['nome'], pedido['kit'], pedido['quantidade'], pedido['valor_kit'], pedido['frete'], pedido['valor_pago'], pedido['pagamento'], pedido['valor_faltante']))

    def adicionar_despesa(self):
        descricao = self.entry_descricao.get()
        valor = self.entry_valor.get()
        if descricao and valor:
            self.despesas.append({'descricao': descricao, 'valor': valor})
            self.tree_despesas.insert("", tk.END, values=(descricao, valor))  # Adicionando a despesa à treeview
            self.entry_descricao.delete(0, tk.END)  # Limpa o campo de descrição
            self.entry_valor.delete(0, tk.END)  # Limpa o campo de valor

    def mostrar_total_despesas(self):
        total = sum(float(despesa['valor']) for despesa in self.despesas)  # Calculando o total das despesas
        print(f"Total de Despesas: R$ {total:.2f}")

# Execução da aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = MarmitariaApp(root)
    root.mainloop()
