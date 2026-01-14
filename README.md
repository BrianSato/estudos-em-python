# 📘 Gerenciador de Despesas Pessoais (CLI)

Um projeto em Python desenvolvido para praticar **arquitetura de software, organização de código e boas práticas**, evoluindo de exercícios isolados para uma aplicação real e extensível.

Este projeto foi pensado para crescer de forma incremental, partindo de uma **CLI bem estruturada** e preparada para futura migração para **GUI**.

---

## 🎯 Objetivo do Projeto

Desenvolver um gerenciador de despesas pessoais via terminal que permita:

* Registrar despesas com valor, descrição, categoria e data
* Persistir dados em arquivo JSON
* Consultar, filtrar e analisar gastos
* Servir como projeto de portfólio com foco em organização e evolução

---

## 🧠 Conceitos Aplicados

* Estruturas de dados (`list`, `dict`)
* Modularização e separação de responsabilidades
* Camadas de aplicação (interface, controle, lógica, persistência)
* Validação de entradas do usuário
* Manipulação de datas com `datetime`
* Persistência de dados com JSON
* Commits semânticos e versionamento organizado

---

## 🗂️ Estrutura do Projeto

```
📦 gerenciador_despesas
 ┣ 📜 despesas_principal.py      # Loop principal e orquestração
 ┣ 📜 despesas_menu.py           # Menus da interface CLI
 ┣ 📜 despesas_adicionar.py      # Entrada e criação de despesas
 ┣ 📜 despesas_listar.py         # Exibição formatada de despesas
 ┣ 📜 despesas_filtrar.py        # Regras de filtragem (categoria / período)
 ┣ 📜 processar_filtros.py       # Controlador do fluxo de filtros
 ┣ 📜 resultado_filtros.py       # Tratamento e exibição dos resultados
 ┣ 📜 despesas_calculos.py       # Estatísticas e resumos financeiros
 ┣ 📜 despesas_arquiva.py        # Persistência em arquivo JSON
 ┣ 📜 mensagens.py               # Textos, erros e prompts centralizados
 ┗ 📜 despesas.json              # Base de dados (gerada automaticamente)
```

---

## ⚙️ Funcionalidades Atuais

### 📌 Gerenciamento de Despesas

* Adicionar despesa
* Listar todas as despesas
* Salvar e carregar dados automaticamente

### 📌 Categorias Padronizadas

* Alimentos
* Pagamento de Boletos
* Gastos com o Carro
* Cartão de Crédito
* Outras

### 📌 Filtros

* Filtrar por categoria
* Filtrar por período (data inicial e final)

### 📌 Estatísticas

* Total gasto
* Média de gastos
* Maior despesa
* Menor despesa

---

## 🧩 Arquitetura

O projeto segue uma organização inspirada em padrões reais de desenvolvimento:

```
Interface (CLI)
   ↓
Controladores
   ↓
Regras de Negócio
   ↓
Persistência
```

* A **interface** não contém lógica de negócio
* As **funções de regra** não imprimem dados
* Mensagens e textos são centralizados para fácil manutenção

Essa abordagem facilita:

* manutenção
* testes
* evolução para GUI ou API

---

## ▶️ Como Executar

1. Clone o repositório
2. Certifique-se de ter Python 3.10+
3. Execute:

```bash
python despesas_principal.py
```

O arquivo `despesas.json` será criado automaticamente.

---

## 🚀 Próximos Passos Planejados

* Congelar a versão CLI
* Planejar migração para GUI
* Implementar relatórios visuais
* Possível exportação de dados

---

## 📌 Observação Final

Este projeto foi desenvolvido com foco em **aprendizado contínuo**, priorizando clareza, organização e boas práticas em vez de atalhos rápidos.

Sinta-se à vontade para explorar, clonar ou sugerir melhorias.

---

✍️ *Projeto em evolução — cada commit representa um passo consciente de aprendizado.*
