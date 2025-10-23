#Desafio 3: Faturamento distribuidora

import json
import math 

NOME_ARQUIVO = 'Desafio_3/dados.json'

def calcular_estatisticas_faturamento(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            faturamento_mensal = json.load(arquivo)
            
    except FileNotFoundError:
        return "ERRO: Arquivo 'dados.json' não encontrado. Certifique-se de que está no diretório correto."
    except json.JSONDecodeError:
        return "ERRO: O arquivo 'dados.json' não está formatado corretamente como JSON."

    if not faturamento_mensal:
        return "A lista de faturamento está vazia. Não há dados para processar."

    faturamentos_validos = [
        item['valor'] 
        for item in faturamento_mensal 
        if item['valor'] > 0
    ]

    # Verifica se há algum dia com faturamento para evitar divisão por zero
    if not faturamentos_validos:
        print("AVISO: Todos os dias tiveram faturamento zero. Estatísticas limitadas.")
        media_mensal = 0
    else:
        soma_faturamentos = sum(faturamentos_validos)
        dias_com_faturamento = len(faturamentos_validos)
        media_mensal = soma_faturamentos / dias_com_faturamento
    
    todos_valores = [item['valor'] for item in faturamento_mensal]
    
    menor_faturamento = min(todos_valores)
    maior_faturamento = max(todos_valores)
       
    dias_acima_da_media = 0
    
    if media_mensal > 0:
        for item in faturamento_mensal:
            if item['valor'] > media_mensal:
                dias_acima_da_media += 1
            
    
    print("-" * 40)
    print(f"Média Mensal de Faturamento (dias > 0): R$ {media_mensal:,.2f}")
    print("-" * 40)
    print(f"• Menor valor de faturamento no mês: R$ {menor_faturamento:,.2f}")
    print(f"• Maior valor de faturamento no mês: R$ {maior_faturamento:,.2f}")
    print(f"• Número de dias com faturamento superior à média: {dias_acima_da_media}")
    print("-" * 40)


if __name__ == "__main__":
    calcular_estatisticas_faturamento(NOME_ARQUIVO)