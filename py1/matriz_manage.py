def exibir_matriz(matriz):
    for linha in matriz:
        print(" ".join(str(elem) for elem in linha))
    print()

def espelhar_vertical(matriz):
    n = len(matriz)
    nova = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            nova[i][j] = matriz[n - 1 - i][j]
    return nova

def espelhar_horizontal(matriz):
    n = len(matriz)
    nova = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            nova[i][j] = matriz[i][n - 1 - j]
    return nova

def girar_90(matriz):
    n = len(matriz)
    nova = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            nova[j][n - 1 - i] = matriz[i][j]
    return nova

def girar_180(matriz):
    # ou aplicar girar_90 duas vezes
    n = len(matriz)
    nova = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            nova[n - 1 - i][n - 1 - j] = matriz[i][j]
    return nova

def ler_matriz():
    n = int(input("Digite o tamanho da matriz quadrada (n x n): "))
    matriz = []
    print("Digite os elementos da matriz linha por linha, separados por espaço:")
    for i in range(n):
        linha = list(map(int, input(f"Linha {i + 1}: ").split()))
        if len(linha) != n:
            print("Erro: A linha deve conter exatamente", n, "elementos.")
            return ler_matriz()  # Repetir a entrada em caso de erro
        matriz.append(linha)
    return matriz

# Exemplo de uso
matriz = ler_matriz()

while True:
    op = int(input("Escolha uma opção (1-4), 1 espelha vertical, 2 espelha horizontal, 3 gira 90º, 4 gira 180º, outro para encerrar: "))

    if op == 1:
        print("Espelho vertical (cabeça para baixo):")
        exibir_matriz(espelhar_vertical(matriz))
    elif op == 2:
        print("Espelho horizontal (espelho):")
        exibir_matriz(espelhar_horizontal(matriz))
    elif op == 3:
        print("Girada 90° (horário):")
        exibir_matriz(girar_90(matriz))
    elif op == 4:
        print("Girada 180°:")
        exibir_matriz(girar_180(matriz))
    else:
        print("Opção de saída!")
        break






