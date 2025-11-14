import sqlite3
import pandas as pd
from typing import List, Dict, Any
from src.domain.entities import Pesquisa

class PesquisaRepository:
    'Gerencia a persistência das entidades Pesquisa no banco de dados SQLite.'
    def __init__(self, db_name='dados_ong_ibis.db'):
        self.db_name = db_name
        'Cria a tabela de pesquisas se não existir.'
        self._setup_db()
    
    def _setup_db(self):
        'Configura a conexão com o banco de dados SQLite.'
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pesquisas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_evento TEXT NOT NULL,
                faixa_etaria TEXT NOT NULL,
                mora_no_bairro INTEGER NOT NULL,
                atividade_favorita TEXT NOT NULL,
                melhoria_sugerida TEXT NOT NULL,
                frequencia TEXT NOT NULL,
                nota_nps INTEGER NOT NULL,
                data_registro TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

        def salvar(self, pesquisa: Pesquisa):
            'Salva uma entidade Pesquisa no banco de dados.'
            pesquisa.validar()

            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            cursor.execute('''
                    INSERT INTO pesquisas (
                        nome_evento,
                        faixa_etaria, 
                        mora_no_bairro,
                        atividade_favorita, 
                        melhoria_sugerida,
                        frequencia, 
                        nota_nps, 
                        data_registro
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', 
                (
                    pesquisa.nome_evento,
                    pesquisa.faixa_etaria,
                    pesquisa.mora_no_bairro,
                    pesquisa.atividade_favorita,
                    pesquisa.melhoria_sugerida,
                    pesquisa.frequencia,
                    pesquisa.nota_nps,
                    pesquisa.data_registro
                )
            )

            conn.commit()
            conn.close()

            def buscar_todos(self) -> pd.DataFrame:
                'Busca todas as pesquisas no BD e retorna para o Pandas DataFrame.'
                conn = sqlite3.connect(self.db_name)
                'Pandas lê SQL e converte para DataFrame.'
                df = pd.read_sql_query(""
                "   SELECT * FROM pesquisas", conn)
                conn.close()
                return df

            def listar_eventos(self) -> pd.DataFrame:
                'Lista os nomes dos eventos únicos presentes no banco de dados.'
                conn = sqlite3.connect(self.db_name)
                cursor = conn.cursor()

                cursor.execute(""
                "   SELECT DISTINCT nome_evento FROM pesquisas WHERE nome_evento IS NOT NULL")
                eventos = [row[0] for row in cursor.fetchall()]
                
                conn.close()
                return eventos