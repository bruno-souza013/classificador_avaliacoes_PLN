import pandas as pd
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split

# Carrega o arquivo CSV
csv_file = 'reviews.csv'
df = pd.read_csv(csv_file)

# Stopwords customizados em português e inglês
custom_stopwords = {
    # Artigos em português
    'o', 'a', 'os', 'as', 'um', 'uma', 'uns', 'umas',
    # Artigos em inglês
    'the', 'a', 'an',
    # Preposições em português
    'de', 'para', 'em', 'com', 'por', 'do', 'da', 'dos', 'das', 'ao', 'às',
    'entre', 'dentro', 'fora', 'sobre', 'sob', 'ante', 'contra', 'através',
    'durante', 'sem', 'até', 'desde', 'perante', 'entre',
    # Preposições em inglês
    'in', 'on', 'at', 'by', 'to', 'from', 'with', 'for', 'of', 'about',
    'into', 'through', 'during', 'before', 'after', 'above', 'below',
    'between', 'under', 'over', 'out', 'off', 'near', 'around', 'along',
    # Conjunções em português
    'e', 'mas', 'ou', 'se', 'quando', 'enquanto', 'pois', 'porque', 'porém',
    'contudo', 'todavia', 'entretanto', 'senão', 'nem', 'quer',
    # Conjunções em inglês
    'and', 'but', 'or', 'if', 'when', 'while', 'though', 'although',
    'because', 'since', 'unless', 'until', 'whereas', 'however', 'yet',
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
    'isso', 'aquilo', 'então', 'também', 'não', 'sim', 'muito', 'pouco', 'muito',
    'todo', 'toda', 'todos', 'todas', 'outro', 'outra', 'outros', 'outras',
    'mesmo', 'mesma', 'mesmos', 'mesmas', 'próprio', 'qual', 'quais', 'quanto',
    'quanta', 'quantos', 'quantas', 'que', 'qual', 'quem', 'onde', 'quando',
    'como', 'aqui', 'ali', 'acolá', 'lá', 'cá', 'talvez', 'somente', 'apenas',
    'já', 'ainda', 'nunca', 'sempre', 'raramente', 'frequentemente',
}

# Combina stopwords padrão com customizados
stop_words = set(stopwords.words('portuguese')).union(custom_stopwords)

def remove_stop_words(text):
    words = text.lower().split()
    filtered_words = [word for word in words if word not in stop_words]
    return ' '.join(filtered_words)


# Processa cada coluna de texto do dataframe
print("Iniciando limpeza do CSV...")
df['review_text_limpo'] = df['review_text'].apply(lambda x: remove_stop_words(str(x)) if pd.notna(x) else '')

# Remove a coluna original, depois de criar a nova coluna limpa
if 'review_text' in df.columns:
    df.drop(columns=['review_text'], inplace=True)

# Salva o novo CSV com os dados limpos
output_file = 'reviews_limpo.csv'
df.to_csv(output_file, index=False)
print(f"Arquivo '{output_file}' gerado com sucesso!")
print(f"Total de linhas processadas: {len(df)}")

# Etapa E: holdout estratificado em treino e teste
train_df, test_df = train_test_split(
    df,
    test_size=0.2,
    random_state=42,
    stratify=df['label']
)

train_file = 'reviews_treino.csv'
test_file = 'reviews_teste.csv'

train_df.to_csv(train_file, index=False)
test_df.to_csv(test_file, index=False)

print(f"Arquivo '{train_file}' gerado com sucesso! Linhas: {len(train_df)}")
print(f"Arquivo '{test_file}' gerado com sucesso! Linhas: {len(test_df)}")
