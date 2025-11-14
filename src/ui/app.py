import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt
import random
from src.domain.entities import Pesquisa

class SistemaONGApp:
    def __init__(self, root, repository):
        self.repo = repository
        self.root = root
        self.root.title("Coleta de Dados - ONG IBIS")
        self.root.geometry("600x750")

        'Inicializa os componentes da interface gráfica.'
        self._montar_tela()

    def _montar_tela(self):
        'Título'
        tk.Label(self.root, text="Pesquisa NPS - ONG IBIS", font=("Calibri", 16, "bold")).pack(pady=15)

        frame = tk.Frame(self.root)
        frame.pack(pady=5, padx=10)

        # --- Campos do formulário ---
        '1. Nome do Evento'
        tk.Label(frame, text="Nome do Evento Atual: ", font=("Calibri", 10, "bold")).grid(row=0, column=0, sticky="e", pady=5)
        self.entry_evento = tk.Entry(frame, width=33)
        self.entry_evento.grid(row=0, column=1, pady=5)
        self.entry_evento.insert(0, "Futebol de Rua") # Valor Padrão para facilitar

        '2. Faixa Etária'
        tk.Label(frame, text="Faixa Etária: ", font=("Calibri", 10, "bold")).grid(row=1, column=0, sticky="e", pady=5)
        self.combo_faixa = ttk.Combobox(frame, values=[
            "Até 12 anos", "13 a 17 anos", "18 a 25 anos", "Acima de 25 anos"], state="readonly", width=30)
        self.combo_faixa.grid(row=1, column=1, pady=5)

        '3. Mora no Bairro'
        tk.Label(frame, text="Mora no Bairro?", font=("Calibri", 10, "bold")).grid(row=2, column=0, sticky="e", pady=5)
        self.combo_bairro = ttk.Combobox(frame, values=["Sim", "Não"], state="readonly", width=30)
        self.combo_bairro.grid(row=2, column=1, pady=5)

        '4. Atividade Favorita'
        tk.Label(frame, text= "Atividade Favorita: ", font=("Calibri", 10, "bold")).grid(row=3, column=0, sticky="e", pady=5)
        self.combo_atividade = ttk.Combobox(frame, values=[
            "Futebol / Futsal", "Dança", "Brincadeiras", "Pintura de Rosto"], state="readonly", width=30)
        self.combo_atividade.grid(row=3, column=1, pady=5)

        '5. Melhoria Sugerida'
        tk.Label(frame, text="Melhoria Sugerida: ", font=("Calibri", 10, "bold")).grid(row=4, column=0, sticky="e", pady=5)
        self.entry_melhoria = ttk.Combobox(frame, values=[
            "Organização / Horários", "Bebedouro / Lanches", "Materiais", "Nada, está tudo ótimo"], state="readonly", width=30)
        self.entry_melhoria.grid(row=4, column=1, pady=5)

        '6. Frequência'
        tk.Label(frame, text="Frequência de Participação: ", font=("Calibri", 10, "bold")).grid(row=5, column=0, sticky="e", pady=5)
        self.combo_frequencia = ttk.Combobox(frame, values=[
            "Primeira vez", "Venho às vezes", "Venho em todos"], state="readonly", width=30)
        self.combo_frequencia.grid(row=5, column=1, pady=5)

        '7. Nota NPS'
        tk.Label(frame, text="Nota NPS (0 a 10): ", font=("Calibri", 10, "bold")).grid(row=6, column=0, sticky="e", pady=5)
        self.entry_nps = tk.Entry(frame, width=33)
        self.entry_nps.grid(row=6, column=1, pady=5)

        # --- Botões ---
        tk.Button(self.root, text="Salvar Pesquisa", command=self.salvar_click, bg="#4CAF50", fg="white", 
                 font=("Calibri", 10, "bold"), width=25).pack(pady=15)
        
        tk.Frame(self.root, height=2, bg="#ddd", width=500).pack(pady=10)

        tk.Label(self.root, text="Área de Gestão", fg="grey").pack()

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="VISUALIZAR DASHBOARD", command=self.ver_dashboard_click,bg="#2196F3", fg="white",
                width=20).grid(row=0, column=0, padx=5) 
        tk.Button(btn_frame, text="[DEV] Gerar dados fake", command=self.gerar_dados_fake, bg="#9E9E9E", fg="white",
                width=20).grid(row=0, column=1, padx=5)
        
    def limpar_campos(self):
        'Limpa os campos do formulário.'
        self.entry_evento.delete(0, tk.END)
        self.combo_faixa.set('')
        self.combo_bairro.set('')
        self.combo_atividade.set('')
        self.entry_melhoria.set('')
        self.combo_frequencia.set('')
        self.entry_nps.delete(0, tk.END)
    
    
    def salvar_click(self):
        'Evento do botão Salvar Pesquisa.'
        try:
            'Trata  o valor do campo NPS para garantir que seja um inteiro.'
            try:
                val_nps = int(self.entry_nps.get())
            except ValueError:
                raise ValueError("A nota NPS deve ser um número inteiro.")
            
            'Trata o valor do campo Mora no Bairro para booleano.'
            text_bairro = self.combo_bairro.get()
            if text_bairro == "Sim":
                bool_bairro = True
            elif text_bairro == "Não":
                bool_bairro = False
            else:
                raise ValueError("O campo 'Mora no Bairro' deve ser respondido com Sim ou Não.")

            'Cria a entidade Pesquisa com os dados do formulário.'
            nova_pesquisa = Pesquisa(
                nome_evento=self.entry_evento.get(),
                faixa_etaria=self.combo_faixa.get(),
                mora_no_bairro=bool_bairro,
                atividade_favorita=self.combo_atividade.get(),
                melhoria_sugerida=self.entry_melhoria.get(),
                frequencia=self.combo_frequencia.get(),
                nota_nps=val_nps
            )
            'Persistência'
            self.repo.salvar(nova_pesquisa)
            messagebox.showinfo("Sucesso", "Pesquisa salva com sucesso!")
            self.limpar_campos()

        except ValueError as e:
            'Exibe mensagem de erro para o usuário.'
            messagebox.showerror("Erro", f"Ocorreu um erro ao salvar a pesquisa: {str(e)}")
        
    def ver_dashboard_click(self):
        df = self.repo.buscar_todos()
        if df.empty:
            messagebox.showwarning("Atenção", "Nenhum dado disponível para exibir o dashboard.")
            return
        
        # Gráfico Simples com Matplotlib
        plt.figure(figsize=(12, 6))
        plt.suptitle("Dashboard: Indicadores de Impacto - ONG IBIS", fontsize=16, fontweight='bold')

        # Gráfico 1:Atividades
        plt.subplot(1, 2, 1)
        df['atividade_favorita'].value_counts().plot(kind='bar', color='purple')
        plt.title("Atividades Favoritas")
        plt.xlabel('')

        # Gráfico 2: Origem dos Participantes
        plt.subplot(1, 2, 2)
        #Mapeia: 1 -> Bairro / 0 -> Fora do Bairro
        nomes_bairro = df['mora_no_bairro'].map({True: 'Bairro', False: 'Fora do Bairro'})
        nomes_bairro.value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['#66b3ff',"#ffbb99"])
        plt.title("Origem dos Participantes")

        plt.tight_layout()
        plt.show()

    def gerar_dados_fake(self):
        'Gera dados fake para testes.'
        evento = self.repo.listar_eventos() or ["Evento Teste"]

        for _ in range(50):
            pesquisa_fake = Pesquisa(
                nome_evento=evento,
                faixa_etaria=random.choice(['Até 12 anos', '13 a 17 anos', '18 a 25 anos']),
                mora_no_bairro=random.choice([True, False]),
                atividade_favorita=random.choice(['Futebol / Futsal', 'Dança', 'Brincadeiras', 'Pintura de Rosto']),
                melhoria_sugerida=random.choice(['Organização / Horários', 'Bebedouro / Lanches', 'Materiais', 'Nada, está tudo ótimo']),
                frequencia=random.choice(['Primeira vez', 'Venho às vezes', 'Venho em todos']),
                nota_nps=random.randint(7, 10)
            )
            self.repo.salvar(pesquisa_fake)
        
        messagebox.showinfo("DEV Mode", f"50 pesquisas fake foram geradas com sucesso para o evento : {evento}!")
