# Desafio 2: Sequência de Fibonacci e Verificação de Pertencimento

def verifica_fibonacci(numero_alvo):
    if numero_alvo < 0:
        return f"O número {numero_alvo} NÃO PERTENCE à sequência de Fibonacci (Sequência inicia em 0)."
        
    if numero_alvo == 0 or numero_alvo == 1:
        return f"O número {numero_alvo} PERTENCE à sequência de Fibonacci."

    a, b = 0, 1

    while b < numero_alvo:
        a, b = b, a + b

    if b == numero_alvo:
        return f"O número {numero_alvo} PERTENCE à sequência de Fibonacci."
    else:
        return f"O número {numero_alvo} NÃO PERTENCE à sequência de Fibonacci."

try:
    
    entrada_usuario = input("Informe um número inteiro para verificar na sequência de Fibonacci: ")
    numero = int(entrada_usuario)
    
    resultado = verifica_fibonacci(numero)
    print(resultado)
    
except ValueError:
    print("ERRO: Entrada inválida. Por favor, insira apenas números inteiros.")