import pandas as pd
import os

# ======================== CONFIGURAÇÕES INICIAIS ======================== #

# Diretório onde estão os arquivos originais .tsv
diretorio_entrada = "~/Desktop/Grafos/data"

# Diretório onde serão salvos os arquivos menores
diretorio_saida = "~/Documents/Github/lcostafranco/graph_data"

# Tamanho de cada arquivo menor (em linhas)
tamanho_chunk = 250000

# Nomes dos arquivos que vamos dividir
arquivos = [
    "title.basics.tsv",
    "title.crew.tsv",
    "name.basics.tsv"
]

# =========================== SCRIPT PRINCIPAL =========================== #

for nome_arquivo in arquivos:
    caminho_entrada = os.path.join(diretorio_entrada, nome_arquivo)
    print(f"Lendo arquivo: {caminho_entrada}")

    # Garantindo que existe diretório de saída
    os.makedirs(diretorio_saida, exist_ok=True)

    # Ler e dividir em partes menores
    with pd.read_csv(caminho_entrada, sep='\t', chunksize=250000) as reader:
        for i, chunk in enumerate(reader):
            # Monta nome do arquivo de saída
            arquivo_saida = f"{nome_arquivo.replace('.tsv', '')}_part_{i+1}.tsv"
            caminho_saida = os.path.join(diretorio_saida, arquivo_saida)

            chunk.to_csv(caminho_saida, sep='\t', index=False)
            print(f"Arquivo salvo: {caminho_saida}")

print("Processamento concluído!")