import unittest
import os
from src.domain.entities import Pesquisa
from src.infra.repository import PesquisaRepository

class TestPesquisaRepository(unittest.TestCase):

    def setUp(self):
        'memory: Cria um repositório temporário em memória para testes.'
        self.db_temp = 'test_banco_temp.db'
        self.repo = PesquisaRepository(db_name=self.db_temp)
    
    def tearDown(self):
        'Remove o banco de dados temporário após os testes.'
        if os.path.exists(self.db_temp):
            os.remove(self.db_temp)
    
    def test_salvar_pesquisa_valida(self):
        'Caminho feliz: salvar uma pesquisa válida no banco de dados.'
        pesquisa = Pesquisa(
            nome_evento="Evento Teste",
            faixa_etaria="18 a 25 anos",
            mora_no_bairro=True,
            atividade_favorita="Pintura de Rosto",
            melhoria_sugerida="Materiais",
            frequencia="Venho às vezes",
            nota_nps=8
        )
        self.repo.salvar(pesquisa)

        df = self.repo.buscar_todos()

        self.assertEqual(len(df), 1) 
        self.assertEqual(df.iloc[0]['nome_evento'], "Evento Teste")
        self.assertEqual(df.iloc[0]['nota_nps'], 8)

    def test_listar_eventos_unicos(self):
        'Caminho feliz: listar eventos únicos do banco de dados.'
        pesquisas = [
            Pesquisa(
                nome_evento="Evento Teste A",
                faixa_etaria="Até 12 anos",
                mora_no_bairro=True,
                atividade_favorita="Futebol / Futsal",
                melhoria_sugerida="Nada, está tudo ótimo",
                frequencia="Venho em todos",
                nota_nps=9
            ),
            Pesquisa(
                nome_evento="Evento Teste B",
                faixa_etaria="13 a 17 anos",
                mora_no_bairro=False,
                atividade_favorita="Brincadeiras",
                melhoria_sugerida="Lanche",
                frequencia="Venho às vezes",
                nota_nps=7
            ),
            Pesquisa(
                nome_evento="Evento Teste A", 
                faixa_etaria="18 a 25 anos",
                mora_no_bairro=True,
                atividade_favorita="Dança",
                melhoria_sugerida="Mais atividades",
                frequencia="Venho em todos",
                nota_nps=10
            )
        ]
        for p in pesquisas:
            self.repo.salvar(p)

        lista = self.repo.listar_eventos()

        self.assertEqual(len(lista), 2)
        self.assertIn("Evento Teste A", lista)
        self.assertIn("Evento Teste B", lista)
    
    def test_buscar_todas_banco_vazio(self):
        'Testa se o sistema lida bem quando não tem nada no banco'
        df = self.repo.buscar_todos()
        self.assertTrue(df.empty) # Tem que retornar vazio, não pode dar erro