# 🏟️ Sistema de Gestão para ONG - Esporte e Vida

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=tinalmeid_CST-ciencia-dados-projeto-extensao-2-semestre&metric=alert_status)](https://sonarcloud.io/dashboard?id=tinalmeid_CST-ciencia-dados-projeto-extensao-2-semestre)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=tinalmeid_CST-ciencia-dados-projeto-extensao-2-semestre&metric=coverage)](https://sonarcloud.io/dashboard?id=tinalmeid_CST-ciencia-dados-projeto-extensao-2-semestre)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=tinalmeid_CST-ciencia-dados-projeto-extensao-2-semestre&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=tinalmeid_CST-ciencia-dados-projeto-extensao-2-semestre)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Architecture](https://img.shields.io/badge/Architecture-DDD%20Lite-orange)](https://en.wikipedia.org/wiki/Domain-driven_design)

## 📋 Sobre o Projeto

Este software foi desenvolvido como parte do **Projeto de Extensão em Ciência de Dados**, visando solucionar a falta de métricas e gestão de dados de uma ONG esportiva em Timóteo/MG.

O sistema permite o cadastro offline de participantes, armazena os dados em banco local (SQLite) e gera Dashboards automáticos para apoio à tomada de decisão e captação de patrocínios.

## 🚀 Tecnologias e Arquitetura

O projeto segue princípios de **Clean Code** e uma arquitetura baseada em **DDD (Domain-Driven Design)** simplificado:

- **Linguagem:** Python 3.x
- **Interface (UI):** Tkinter (Nativo)
- **Banco de Dados:** SQLite
- **Análise de Dados:** Pandas & Matplotlib
- **Qualidade:** Unittest (Testes Automatizados) & SonarCloud

### Estrutura de Camadas

1.  **Domain Layer:** Regras de negócio e validações (Entidade `Pesquisa`).
2.  **Infrastructure Layer:** Persistência de dados (Padrão `Repository`).
3.  **UI Layer:** Interface gráfica para o usuário final.
4.  **Tests:** Garantia de integridade do sistema.

## 🛠️ Como Executar

### Pré-requisitos

- Python 3.10 ou superior instalado.

### Instalação

1.  Clone o repositório:
    ```bash
    git clone [https://github.com/seu-usuario/sistema-ong-ddd.git](https://github.com/seu-usuario/sistema-ong-ddd.git)
    ```
2.  Instale as dependências:
    ```bash
    pip install pandas matplotlib
    ```
3.  Execute o sistema:
    ```bash
    python sistema_ong_ddd.py
    ```
    _Os testes unitários rodarão automaticamente antes da abertura da janela._

## 📊 Funcionalidades

- ✅ Cadastro de Pesquisa de Satisfação (NPS).
- ✅ Validação de Regras de Negócio (Domínio).
- ✅ Geração de Dashboards (Pizza e Barras).
- ✅ Geração de Dados Fictícios (Mock) para testes.

---

**Desenvolvido por:** Cristina de Almeida
