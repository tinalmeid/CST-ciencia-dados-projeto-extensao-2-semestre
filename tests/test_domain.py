import unittest
from src.domain.entities import Pesquisa

class TestPesquisaDomain(unittest.TestCase):
    
    def test_criacao_pesquisa_valida(self):
        'Caminho feliz: criação de uma pesquisa válida.'
        pesquisa = Pesquisa(
            nome_evento="Futebol de Rua",
            faixa_etaria="Até 12 anos",
            mora_no_bairro=True,
            atividade_favorita="Futebol / Futsal",
            melhoria_sugerida="Nada, está tudo ótimo",
            frequencia="Venho em todos",
            nota_nps=9
        )
        'Se validar() não levantar exceção, o teste passa.'
        try:
            pesquisa.validar()
        except ValueError as e:
            self.fail(f"Validação falhou inesperadamente: {e}")
    
    def test_pesquisa_sem_nome_evento(self):
        'Caminho Error: nome do evento ausente.'
        pesquisa = Pesquisa(
            nome_evento="", #Nome do evento vazio
            faixa_etaria="18 a 25 anos",
            mora_no_bairro=True,
            atividade_favorita="Dança",
            melhoria_sugerida="Nada, está tudo ótimo",
            frequencia="Venho em todos",
            nota_nps=10
        )
        with self.assertRaises(ValueError) as context:
            pesquisa.validar()
        self.assertIn("O nome do Evento é obrigatório.", str(context.exception))

    def test_erro_campos_obrigatorios_vazios(self):
        'Caminho Error: campos obrigatórios vazios.'
        pesquisa = Pesquisa(
            nome_evento="Futebol de Rua",
            faixa_etaria="", #Faixa etária vazia
            mora_no_bairro=False,
            atividade_favorita="", #Atividade favorita vazia
            melhoria_sugerida="Materiais",
            frequencia="Venho às vezes",
            nota_nps=8
        )
        with self.assertRaises(ValueError) as context:
            pesquisa.validar()
        self.assertIn("Campos obrigatórios (Faixa Etária ou Atividade Favorita) estão vazios.", str(context.exception))

    def test_erro_bairro_tipo_invalido(self):
        'Caminho Error: valor inválido para mora_no_bairro.'
        pesquisa = Pesquisa(
            nome_evento="Futebol de Rua",
            faixa_etaria="13 a 17 anos",
            mora_no_bairro="", #mora_no_bairro vazio
            atividade_favorita="Brincadeiras",
            melhoria_sugerida="Lanche",
            frequencia="Venho em todos",
            nota_nps=8
        )
        with self.assertRaises(ValueError) as context:
            pesquisa.validar()
        self.assertIn("O campo 'Mora no Bairro' deve ser respondido com Sim ou Não.", str(context.exception))

    def test_nps_fora_intervalo(self):
        'Caminho Error: nota NPS fora do intervalo permitido.'
        pesquisa = Pesquisa(
            nome_evento="Futebol de Rua",
            faixa_etaria="Até 12 anos",
            mora_no_bairro=True,
            atividade_favorita="Futebol / Futsal",
            melhoria_sugerida="Organização / Horário",
            frequencia="Venho às vezes",
            nota_nps=15 #Nota NPS inválida
        )
        with self.assertRaises(ValueError) as context:
            pesquisa.validar()
        self.assertIn("A nota NPS deve estar entre 0 e 10.", str(context.exception))
