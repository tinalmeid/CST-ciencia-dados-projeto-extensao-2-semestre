from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Pesquisa:
    'Entidade que representa a pesquisa realizada pela ONG no evento.'
    id: Optional[int] = None
    nome_evento: Optional[str] = None
    faixa_etaria: Optional[str] = None
    mora_no_bairro: Optional[bool] = None
    atividade_favorita: Optional[str] = None
    melhoria_sugerida: Optional[str] = None
    frequencia : Optional[str] = None
    nota_nps: Optional[int] = None
    data_registro: Optional[datetime] = None

    'Trata a inicializacao da dataclass. '
    'Transforma data_registro em formato string.'
    def __post_init__(self):
        if self.data_registro is None:
            self.data_registro = datetime.now().strftime("%Y-%m-%d")

    def validar(self):
        'Valida os atributos da entidade Pesquisa (Invariant)'
        if not self.nome_evento:
            raise ValueError("O nome do Evento é obrigatório.")
        
        if not self.faixa_etaria or not self.atividade_favorita:
            raise ValueError("Campos obrigatórios (Faixa Etária ou Atividade Favorita) estão vazios.")
        
        if not isinstance(self.mora_no_bairro, bool):
            raise ValueError("O campo 'Mora no Bairro' deve ser respondido com Sim ou Não.")
        
        if not self.frequencia or not self.melhoria_sugerida:
            raise ValueError("Campos obrigatórios (Frequência ou Melhoria Sugerida) estão vazios.")
        
        if not isinstance(self.nota_nps, int):
            raise ValueError("A nota NPS deve ser um número inteiro.")
        
        if not (0 <= self.nota_nps <= 10):
            raise ValueError("A nota NPS deve estar entre 0 e 10.")
        
    
        
