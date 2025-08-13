import os 
import camelot
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from pathlib import Path

arquivo = 'Redrex - Fatura (1)'
# Monta o caminho completo até o PDF, independente do sistema operacional
path = Path(__file__).parent / "files" / "pdf" / "RedRex" / f"{arquivo}.pdf"

# Lê todas as tabelas do PDF (páginas 1 até o fim), usando o método "stream"
# "stream" é indicado quando não há linhas visíveis delimitando a tabela
tables = camelot.read_pdf(
    path,
    pages='1-end',
    flavor= 'stream',
    table_areas=['70, 558,516, 313'],
    columns=["70, 106, 155, 214, 280, 331, 383, 445"],
    strip_text=" .\n"
)

# Mostra o relatório de parsing (qualidade da detecção da tabela)
print(tables[0].parsing_report)

# Gera uma visualização gráfica dos contornos da tabela detectada
camelot.plot(tables[0], kind="contour")

# Exibe o gráfico na tela
plt.show()

# print(tables[0].df) # result. no terminal

# Pausa simbólica (apenas imprime texto)
print("Pause")