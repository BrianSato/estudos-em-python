# 📘 Semana 4 – Projeto Gerenciador de Despesas Pessoais

Nesta semana, iniciei o desenvolvimento de um projeto prático em Python, aplicando de forma integrada os conceitos estudados até agora.
O foco foi sair de exercícios isolados e trabalhar em um sistema simples, porém real, simulando um gerenciador de despesas pessoais via terminal.

---
# 🎯 Objetivos da Semana

 - Consolidar o uso de listas, dicionários e funções
 - Criar um programa baseado em menu interativo
 - Trabalhar com organização e evolução incremental do código
 - Aplicar lógica para cálculos financeiros simples
 - Introduzir boas práticas de estruturação de código
 - Preparar base para persistência de dados (arquivos)
---
# 🧠 Conceitos Aplicados

 - Funções (def)
 - Estruturas condicionais (if / elif / else)
 - Laços de repetição (while, for)
 - Listas (list)
 - Dicionários (dict)
 - Entrada e saída de dados (input, print)
 - Organização de código por responsabilidade
 - Tratamento básico de erros (try / except)
---
# 🧾 Funcionalidades do Projeto

 - O sistema funciona via menu no terminal, permitindo:
 - Adicionar despesas
 - Valor da despesa
 - Descrição da despesa
 - Listar todas as despesas cadastradas
 - Exibir estatísticas, como:
 - Total gasto
 - (Em evolução) média, maior e menor despesa
 - Encerrar o programa
---
As despesas são armazenadas em uma lista de dicionários, no formato:
```bash
{
    "valor": 50.0,
    "descricao": "Mercado"
}
```
## 🗂️ Organização do Projeto

O projeto passou a ser estruturado em módulos, seguindo boas práticas de organização em Python:

- `despesas_principal.py`: responsável pelo menu e fluxo principal do programa
- `despesas_funcoes.py`: contém as funções relacionadas ao gerenciamento das despesas

Essa separação melhora a legibilidade, manutenção e escalabilidade do código.

---
# 🛠️ Estrutura do Projeto
```bash
semana-4-gerenciador-despesas/
├── despesas_principal.py
├── despesas_funcoes.py
├── README.md
└── dados.txt   (em desenvolvimento)
```
---
# 🚀 Evolução Planejada

Ao longo da semana, o projeto será incrementado com:

 - Estatísticas mais completas
 - Salvamento de dados em arquivo
 - Carregamento automático das despesas
 - Refatoração do código
 - Melhorias de legibilidade e organização
---
# 📌 Observações

Este projeto faz parte da minha jornada de aprendizado em Python, com foco em:

 - lógica de programação
 - construção de projetos reais
 - desenvolvimento progressivo
 - boas práticas iniciais de código

Cada versão representa uma evolução do entendimento e da aplicação dos conceitos estudados.
