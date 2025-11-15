import tkinter as tk
import unittest
import sys

# Importando as camadas
from src.infra.repository import PesquisaRepository
from src.ui.app import SistemaONGApp

if __name__ == "__main__":
    print("--------------------------------------------------")
    print("🚀 INICIANDO SISTEMA DE GESTÃO - ONG ESPORTE E VIDA")
    print("--------------------------------------------------")

# 1. AUTO-VERIFICAÇÃO (Self-Test)
    # Roda os testes unitários antes de deixar o usuário entrar.
    print("🔍 Executando testes de integridade (Quality Gate)...")
    
    loader = unittest.TestLoader()
    # Procura testes na pasta 'tests' e define a raiz '.' como diretório base
    suite = loader.discover(start_dir='tests', top_level_dir='.')
    
    # verbosity=1 deixa o log mais limpo
    runner = unittest.TextTestRunner(verbosity=1)
    result = runner.run(suite)

    if result.wasSuccessful():
        print("\n✅ TESTES APROVADOS! O sistema está seguro.")
        print("--------------------------------------------------")
        print("Abrindo interface gráfica...")
        
        # 2. INJEÇÃO DE DEPENDÊNCIA
        # Cria o repositório (Banco)
        repo = PesquisaRepository()
        
        # 3. INICIALIZAÇÃO DA UI
        # Cria a janela e passa o repositório para a aplicação
        root = tk.Tk()
        app = SistemaONGApp(root, repo)
        
        # Mantém a janela aberta
        root.mainloop()
        
    else:
        print("\n❌ ERRO CRÍTICO: Falha nos testes de integridade.")
        print("O sistema foi bloqueado para evitar corrupção de dados.")
        print("Consulte o log acima para detalhes.")
        sys.exit(1)