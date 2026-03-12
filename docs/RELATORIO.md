
# Relatório Técnico-Científico

## Capa

**Título:** Classificação Automática de Avaliações de Produtos Utilizando Técnicas de Processamento de Linguagem Natural

**Disciplina:** [Preencher]

**Aluno:** [Preencher]

**Professor:** [Preencher]

**Instituição:** [Preencher]

**Data:** 12 de março de 2026

---

## Sumário

1. Introdução
2. Fundamentação Teórica
3. Metodologia
    3.1 Coleta de Dados
    3.2 Limpeza e Pré-processamento
    3.3 Tokenização
    3.4 Divisão dos Dados
4. Resultados Parciais
5. Considerações Finais
6. Referências

---

## 1. Introdução

O avanço das tecnologias de Processamento de Linguagem Natural (PLN) tem permitido a análise automatizada de grandes volumes de textos, como avaliações de produtos em plataformas de e-commerce. Este relatório apresenta o desenvolvimento de um sistema de classificação automática de avaliações, com o objetivo de categorizar opiniões de consumidores em positivas, neutras ou negativas, utilizando técnicas de PLN e aprendizado de máquina. O projeto foi desenvolvido com base em dados reais extraídos do site "Beleza na Web".

---

## 2. Fundamentação Teórica

O Processamento de Linguagem Natural é uma subárea da Inteligência Artificial que visa possibilitar a comunicação entre humanos e computadores por meio da linguagem natural. Entre as tarefas mais comuns do PLN estão a remoção de stopwords, tokenização, análise de sentimentos e classificação de textos. A classificação de sentimentos, em particular, é amplamente utilizada para entender a percepção dos usuários sobre produtos e serviços, auxiliando empresas na tomada de decisões estratégicas.

O uso de técnicas como a remoção de stopwords e a tokenização permite a redução de ruídos e a extração de informações relevantes dos textos. A divisão dos dados em conjuntos de treinamento e teste é fundamental para avaliar o desempenho de modelos preditivos, garantindo a generalização dos resultados.

---

## 3. Metodologia

### 3.1 Coleta de Dados

A primeira etapa do projeto consistiu na coleta de avaliações de produtos no site "Beleza na Web". As avaliações foram extraídas manualmente e classificadas conforme a nota atribuída pelo usuário:
- 4-5 estrelas: Avaliação positiva
- 3 estrelas: Avaliação neutra
- 1-2 estrelas: Avaliação negativa

Os dados foram organizados em um arquivo CSV, contendo o texto da avaliação e a respectiva classificação, visando facilitar o processamento automatizado nas etapas seguintes.

### 3.2 Limpeza e Pré-processamento

Para garantir a qualidade dos dados, foi realizada uma etapa de limpeza utilizando a biblioteca NLTK. Foram removidas palavras irrelevantes (stopwords), como artigos, preposições, conjunções, pronomes e termos de uso frequente (ex: "isso", "aquilo", "então", "porque"). Essa etapa é essencial para reduzir o ruído e melhorar a performance dos algoritmos de classificação.

### 3.3 Tokenização

Após a limpeza, cada avaliação foi segmentada em palavras (tokens), processo conhecido como tokenização. Essa transformação é fundamental para que os algoritmos de PLN possam manipular e analisar os textos de forma estruturada. O resultado da tokenização foi salvo em um novo arquivo CSV, permitindo a rastreabilidade e a análise dos dados processados.

### 3.4 Divisão dos Dados

Com os dados tokenizados, realizou-se a divisão do conjunto em duas partes: treinamento e teste. Utilizou-se o método de holdout estratificado, que assegura a proporcionalidade das classes em ambos os conjuntos, evitando viés e garantindo uma avaliação mais precisa do desempenho do modelo.

---

## 4. Resultados Parciais

Até o momento, todas as etapas de preparação dos dados foram concluídas com sucesso. Os dados encontram-se prontos para a aplicação de algoritmos de classificação, que serão implementados nas próximas fases do projeto. A expectativa é que, com a base devidamente tratada, o modelo apresente resultados satisfatórios na tarefa de classificação de sentimentos.

---

## 5. Considerações Finais

O desenvolvimento deste projeto proporcionou uma visão prática sobre as etapas fundamentais do PLN, desde a coleta e preparação dos dados até a estruturação para treinamento de modelos. A correta execução dessas etapas é determinante para o sucesso de sistemas de classificação automática. Futuramente, pretende-se implementar e avaliar diferentes algoritmos de classificação, bem como analisar métricas de desempenho como acurácia, precisão e recall.
