# Desafio 5: Inversão de String

def inverte_string(s_original):
    string_invertida = ""
    tamanho = len(s_original)

    for i in range(tamanho - 1, -1, -1):
        string_invertida += s_original[i]
        
    return string_invertida

def executa_desafio_5():
    string_de_entrada = input("Digite a string que deseja inverter: ")
    
    if not string_de_entrada:
        print("A string de entrada está vazia.")
        return
    
    resultado_invertido = inverte_string(string_de_entrada)
    
    print("-" * 30)
    print(f"String Original:  {string_de_entrada}")
    print(f"String Invertida: {resultado_invertido}")
    print("-" * 30)

if __name__ == "__main__":
    executa_desafio_5()