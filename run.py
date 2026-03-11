import sys
import os
from pathlib import Path

# Obtém o diretório raiz do projeto
project_root = Path(__file__).parent.absolute()
src_path = project_root / 'src'

# Adiciona src ao path
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

# Importação do módulo principal
from limpeza_nltk import main  # type: ignore

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        sys.exit(1)
