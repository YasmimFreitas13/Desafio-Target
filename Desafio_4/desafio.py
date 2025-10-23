# Desafio 4: Cálculo do Percentual de Representação por Estado

def calcula_percentual_faturamento():
    faturamento_por_estado = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }
    
    print("-" * 50)
    print("Faturamento Mensal Detalhado:")
    for estado, faturamento in faturamento_por_estado.items():
        print(f"  {estado} – R$ {faturamento:,.2f}")
    print("-" * 50)
    valor_total = sum(faturamento_por_estado.values())
    
    print(f"VALOR TOTAL MENSAL: R$ {valor_total:,.2f}\n")
    print("Percentual de Representação por Estado:")
    print("-" * 50)

    for estado, faturamento in faturamento_por_estado.items():
        percentual = (faturamento / valor_total) * 100
        print(f"  {estado}: {percentual:.2f}%")


if __name__ == "__main__":
    calcula_percentual_faturamento()