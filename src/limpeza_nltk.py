import pandas as pd
import nltk
import os
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
        'contudo', 'todavia', 'entretanto', 'senão', 'nem', 'quer',
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
    
    # Carrega arquivo CSV
    csv_file = project_root / 'data' / 'raw' / 'reviews.csv'
    print(f"Carregando arquivo: {csv_file}")
    df = pd.read_csv(csv_file)
    
    # ETAPA C: Limpeza de dados
    print("ETAPA C: Removendo Stopwords")
    df['review_text_limpo'] = df['review_text'].apply(
        lambda x: remove_stop_words(str(x), stop_words) if pd.notna(x) else ''
    )
    
    # Remove a coluna original
    if 'review_text' in df.columns:
        df.drop(columns=['review_text'], inplace=True)
    
    # Salva dados limpos
    output_file = project_root / 'data' / 'processed' / 'reviews_limpo.csv'
    output_file.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_file, index=False)
    print(f"✓ Arquivo '{output_file.name}' gerado com sucesso!")
    print(f"  Total de linhas processadas: {len(df)}\n")
    
    # ETAPA D: Tokenização
    print("ETAPA D: Tokenização")
    
    df['tokens'] = df['review_text_limpo'].apply(tokenize_text)
    df['tokens_str'] = df['tokens'].apply(lambda x: ' | '.join(x) if x else '')
    
    # Salva CSV com demonstração de tokenização
    tokenization_file = project_root / 'data' / 'processed' / 'tokenizacao_demonstracao.csv'
    tokenized_df = df[['review_text_limpo', 'tokens_str']].copy()
    tokenized_df.columns = ['Texto Limpo', 'Tokens Separados']  # type: ignore
    tokenized_df.to_csv(tokenization_file, index=False)
    print(f"✓ Arquivo '{tokenization_file.name}' gerado com sucesso!")
    
    if len(df) > 0:
        print(f"\n  Exemplo de tokenização:")
        print(f"  Texto: {df['review_text_limpo'].iloc[0][:70]}...")
        print(f"  Tokens: {df['tokens_str'].iloc[0][:70]}...\n")
    
    df.drop(columns=['tokens_str'], inplace=True)
    
    # ETAPA E: Divisão treino/teste
    print("ETAPA E: Divisão Treino/Teste (Holdout Estratificado)")
    
    train_df, test_df = train_test_split(
        df,
        test_size=0.2,
        random_state=42,
        stratify=df['label']
    )
    
    train_file = project_root / 'data' / 'train_test' / 'reviews_treino.csv'
    test_file = project_root / 'data' / 'train_test' / 'reviews_teste.csv'
    
    train_file.parent.mkdir(parents=True, exist_ok=True)
    train_df.to_csv(train_file, index=False)
    test_df.to_csv(test_file, index=False)
    
if __name__ == '__main__':
    main()
