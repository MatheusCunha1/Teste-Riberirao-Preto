def fibonacci_sequence(n):
    a, b = 0, 1
    while b <= n:
        if b == n:
            return True
        a, b = b, a + b
    return False

numero = 21
mensagem = f"pertence" if fibonacci_sequence(numero) else "não pertence"
print(f"O número {numero} {mensagem} à sequência de Fibonacci.")
