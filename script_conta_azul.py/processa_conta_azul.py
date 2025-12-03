import sys

file_location = sys.argv[1]
usuario = sys.argv[2]
setor = sys.argv[3]
modo = sys.argv[4]  # REAL ou TESTE

print(f"Upload realizado por: {usuario} | Setor: {setor}")
print(f"Modo de execução: {modo}")
print("--------------------------------------------------")

import sys

file_location = sys.argv[1]
usuario = sys.argv[2]
setor = sys.argv[3]

print(f"Upload realizado por: {usuario} | Setor: {setor}")
