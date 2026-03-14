# Classificador de Avaliações - PLN

Sistema de classificação de avaliações de produtos utilizando Processamento de Linguagem Natural (PLN).

## 📁 Estrutura do Projeto

```
classificador_avaliacoes_PLN/
├── data/                          # Dados do projeto
│   ├── raw/                       # Dados brutos originais
│   │   └── reviews.csv
│   ├── processed/                 # Dados processados/limpos
│   │   ├── reviews_limpo.csv
│   │   └── tokenizacao_demonstracao.csv
│   └── train_test/               # Dados de treino e teste
│       ├── reviews_treino.csv
│       └── reviews_teste.csv
├── src/                           # Scripts e módulos Python
│   ├── __init__.py
│   └── limpeza_nltk.py           # Pipeline principal
├── docs/                          # Documentação
|   └── PASSOS.md                  # Registro das etapas completadas
├── run.py                         # Script para executar o pipeline
├── requirements.txt               # Dependências do projeto
├── LICENSE
├── .gitignore
└── README.md                      # Este arquivo
```

## 🔄 Etapas do Projeto

- [x] **a** - Coleta de Reviews no site Beleza na Web
  - Parâmetros: 4-5 estrelas (Positivo), 3 estrelas (Neutro), 1-2 estrelas (Negativo)
  
- [x] **b** - Limpeza de dados e remoção de stopwords
  - Utiliza NLTK.stopwords() com customizações para português
  
- [x] **c** - Tokenização (divisão em palavras)
  - Gera arquivo CSV demonstrando cada tokenização
  
- [x] **d** - Divisão em treino/teste
  - Holdout estratificado com 70% treino, 30% teste
  
- [x] **e** - Relatório completo

## 🚀 Como Executar

### Instalação de dependências
```bash
pip install -r requirements.txt
```

### Execução do pipeline
```bash
python run.py
```

Ou executar diretamente o módulo:
```bash
python src/limpeza_nltk.py
```

## 📊 Arquivos de Dados

| Arquivo | Localização | Descrição |
|---------|-------------|-----------|
| `reviews.csv` | `data/raw/` | Dados brutos coletados |
| `reviews_limpo.csv` | `data/processed/` | Dados com stopwords removidas |
| `tokenizacao_demonstracao.csv` | `data/processed/` | Demonstração da tokenização com tokens separados |
| `reviews_treino.csv` | `data/train_test/` | 80% dos dados para treino |
| `reviews_teste.csv` | `data/train_test/` | 20% dos dados para teste |

## 🎯 Processo de Limpeza

1. Carrega arquivo bruto do `data/raw/`
2. Remove stopwords em português (artigos, preposições, pronomes, etc.)
3. Salva resultado limpo em `data/processed/`
4. Divide dados em treino/teste e salva em `data/train_test/`

## 📝 Requisitos

- Python 3.7+
- pandas
- nltk
- scikit-learn
