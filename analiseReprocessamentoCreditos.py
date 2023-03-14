import re

with open('relatorio.txt', 'r') as f:
    relatorio = f.read()

# Remove todas as linhas que contêm a palavra "SUCESSO" até a linha ">>>>>>>
# REPROCESSANDO VALIDACOES DE CREDITO COM ERRO <<<<<<<<" ser encontrada
linhas = relatorio.split('\n')
novo_relatorio = ''
remover_linhas = False
for linha in linhas:
    if '>>>>>>>' in linha:
        remover_linhas = False
    if 'SUCESSO' in linha and remover_linhas:
        continue
    if 'ERRO' in linha or 'NAO PROCESSADO' in linha:
        novo_relatorio += linha + '\n'
        remover_linhas = True

# Cria um relatório txt de todos os créditos que foram processados com erro,
# mostrando todos os processamentos da mesma linha
parcelamentos = {}
padrao_linha = re.compile(r'linha=(\d+)')
for linha in novo_relatorio.split('\n'):
    if 'ERRO' in linha or 'NAO PROCESSADO' in linha:
        numero_linha = padrao_linha.search(linha).group(1)
        if numero_linha not in parcelamentos:
            parcelamentos[numero_linha] = []
        parcelamentos[numero_linha].append(linha)

with open('relatorio_erros.txt', 'w') as f:
    for parcelamento in parcelamentos.values():
        f.write('\n'.join(parcelamento) + '\n')
