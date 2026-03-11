import pandas as pd
import nltk
import os
import re
import string
from pathlib import Path

nltk.download('stopwords')
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split

def get_project_root():
    """Retorna o diretório raiz do projeto"""
    return Path(__file__).parent.parent

def remove_stop_words(text, stop_words):
    """Remove stopwords do texto"""
    words = text.lower().split()
    filtered_words = [word for word in words if word not in stop_words]
    return ' '.join(filtered_words)

def remove_excessive_punctuation(text):
    """Reduz sequências de pontuação repetida para uma única ocorrência."""

    if pd.isna(text) or text == '':
        return text
    # Colapsa repetições idênticas: '!!!' -> '!'
    text = re.sub(r'([^\w\s])\1+', r'\1', text)
    # Colapsa sequências mistas de pontuação: '!?!?' -> primeiro caractere
    text = re.sub(r'[^\w\s]{2,}', lambda m: m.group(0)[0], text)
    return text

def tokenize_text(text):
    """Tokeniza o texto em palavras individuais"""
    if pd.isna(text) or text == '':
        return []
    return text.lower().split()

def main():
    """Função principal do pipeline de processamento"""
    
    # Configuração de caminhos
    project_root = get_project_root()
    
    # Stopwords customizados em português e inglês
    custom_stopwords = {
        # Artigos em português
        'o', 'a', 'os', 'as', 'um', 'uma', 'uns', 'umas',
        # Preposições em português
        'de', 'para', 'em', 'com', 'por', 'do', 'da', 'dos', 'das', 'ao', 'às',
        'entre', 'dentro', 'fora', 'sobre', 'sob', 'ante', 'contra', 'através',
        'durante', 'sem', 'até', 'desde', 'perante', 'entre',
        # Conjunções em português
        'e', 'mas', 'ou', 'se', 'quando', 'enquanto', 'pois', 'porque', 'porém',
        'contudo', 'todavia', 'entretanto', 'nem', 'quer',
        # Pronomes em português
        'eu', 'você', 'ele', 'ela', 'nós', 'vós', 'eles', 'elas', 'meu', 'minha',
        'teu', 'tua', 'seu', 'sua', 'nosso', 'nossa', 'dele', 'dela', 'deles', 'delas',
        'me', 'te', 'se', 'nos', 'vos', 'lhe', 'lhes', 'mim', 'ti', 'si',
        'comigo', 'contigo', 'consigo', 'conosco', 'convosco',
        # Verbos auxiliares em português
        'é', 'são', 'era', 'eram', 'foi', 'foram', 'ser', 'estar', 'estou', 'está',
        'estamos', 'estão', 'estava', 'estavam', 'estive', 'estivemos', 'estiveram',
        'tenho', 'tem', 'temos', 'têm', 'tinha', 'tinham', 'tive', 'teve', 'tivemos',
        'tiveram', 'devo', 'deve', 'devemos', 'devem', 'deveria', 'deveriam',
        # Outras palavras de uso frequente em português
        'isso', 'aquilo', 'então', 'também', 'sim',
        'todo', 'toda', 'todos', 'todas', 'outro', 'outra', 'outros', 'outras',
        'mesmo', 'mesma', 'mesmos', 'mesmas', 'próprio', 'qual', 'quais', 'quanto',
        'quanta', 'quantos', 'quantas', 'que', 'qual', 'quem', 'onde', 'quando',
        'como', 'aqui', 'ali', 'acolá', 'lá', 'cá', 'talvez', 'somente', 'apenas',
        'já', 'ainda', 'raramente', 'frequentemente',
    }
    
    # Combina stopwords padrão com customizados
    stop_words = set(stopwords.words('portuguese')).union(custom_stopwords)
    # Manter o "não" para preservar a negação
    stop_words.discard('não')
    
    # Carrega arquivo CSV
    csv_file = project_root / 'data' / 'raw' / 'reviews.csv'
    print(f"Carregando arquivo: {csv_file}")
    df = pd.read_csv(csv_file)
    
    # ETAPA C: Limpeza de dados
    print("ETAPA C: Removendo Stopwords e normalizando pontuação")
    df['review_text_limpo'] = df['review_text'].apply(
        lambda x: remove_stop_words(remove_excessive_punctuation(str(x)), stop_words) if pd.notna(x) else ''
    )
    
    # Remove a coluna original
    if 'review_text' in df.columns:
        df.drop(columns=['review_text'], inplace=True)
    
    # Salva dados limpos
    output_file = project_root / 'data' / 'processed' / 'reviews_limpo.csv'
    output_file.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_file, index=False)
    print(f"  Total de linhas processadas: {len(df)}\n")
    
    # ETAPA D: Tokenização
    print("ETAPA D: Tokenização")
    
    df['tokens'] = df['review_text_limpo'].apply(tokenize_text)

    # Salva CSV com demonstração de tokenização (tokens como array/lista)
    tokenization_file = project_root / 'data' / 'processed' / 'tokenizacao_demonstracao.csv'
    tokenized_df = df[['rating','label', 'tokens']].copy()
    tokenized_df.columns = ['rating','label','tokens'] 
    tokenized_df.to_csv(tokenization_file, index=False)
    
    # ETAPA E: Divisão treino/teste
    print("ETAPA E: Divisão Treino/Teste (Holdout Estratificado)")
    
    train_df, test_df = train_test_split(
        df,
        test_size=0.3,
        random_state=42,
        stratify=df['label']
    )
    
    train_file = project_root / 'data' / 'train_test' / 'reviews_treino.csv'
    test_file = project_root / 'data' / 'train_test' / 'reviews_teste.csv'
    
    cols_to_save = ['rating', 'label', 'tokens']
    train_file.parent.mkdir(parents=True, exist_ok=True)
    train_df.to_csv(train_file, index=False, columns=cols_to_save)
    test_df.to_csv(test_file, index=False, columns=cols_to_save)
    
if __name__ == '__main__':
    main()
