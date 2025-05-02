from PIL import Image
import numpy as np
import os

# Operações matriciais:
def espelhar_vertical(matriz):
    n = len(matriz)
    nova = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            nova[i][j] = matriz[n - 1 - i][j]
            # Inverte a ordem das linhas(que equivale a inverter os elementos das colunas), como se virasse a imagem “de cabeça para baixo”;
            # Isso através da operação "n-1-i";;
            # Exemplo: ordem35 - 1 - linha 0 = 34. Isto é, linha 0 vira linha 34, ou seja, a primeira linha vira a última;
    return nova

def espelhar_horizontal(matriz):
    n = len(matriz)
    nova = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            nova[i][j] = matriz[i][n - 1 - j]
            # Inverte a ordem das colunas(que equivale a inverter os elementos das linhas), como se passasse por um espelho;
            # Isso através da operação "n-1-j";
            # O exemplo é equivalente ao anterior, mas com colunas;
    return nova

def girar_90(matriz):
    n = len(matriz)
    nova = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            nova[j][n - 1 - i] = matriz[i][j]
            # Inverte a ordem das linhas e só depois transpõe-se a matriz;
            # Visualmente é como se a 1º coluna invertesse seus elementos e então se tornasse a 1º linha;
            # Ou seja, a 1º coluna invertida vira a 1º linha;
    return nova

def girar_180(matriz):
    n = len(matriz)
    nova = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            nova[n - 1 - i][n - 1 - j] = matriz[i][j]
            # Inverte-se tanto a ordem das linhas quanto das colunas, como se a imagem fosse girada em 180º;
            # Ou seja, vira de cabeça para baixo e espelha;
    return nova

def girar_menos_90(matriz):
    n = len(matriz)
    nova = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            nova[n - 1 - j][i] = matriz[i][j]
            # Inverte a ordem das colunas e só depois transpõe-se a matriz;
            # Visualmente é como se a 1º linha invertesse seus elementos e então se tornasse a primeira coluna;
            # Ou seja, a 1º linha invertida torna-se a 1º coluna;
    return nova

# Funções de I/O e exibição:
def carregar_imagem_para_matriz(caminho_imagem, mode='L'):
    imagem = Image.open(caminho_imagem).convert(mode)
    matriz = np.array(imagem)
    return matriz, mode

def salvar_matriz_como_imagem(matriz, modo, caminho_saida):
    # Garante extensão válida
    root, ext = os.path.splitext(caminho_saida)
    if ext.lower() not in ['.png', '.jpg', '.jpeg', '.bmp', '.pbm', '.gif', '.tiff']:
        caminho_saida = f"{caminho_saida}.png"
    imagem_resultado = Image.fromarray(matriz.astype(np.uint8), mode=modo)
    imagem_resultado.save(caminho_saida)

def exibir_matriz(matriz, max_display=1500):
    h, w = matriz.shape[:2]
    print(f"Matriz de dimensão {h}x{w}")
    rows = min(max_display, h)
    cols = min(max_display, w)
    for i in range(rows):
        linha = matriz[i, :cols]
        # se imagem colorida, mostra média de canais
        if linha.ndim == 1:
            vals = linha
        else:
            vals = linha.mean(axis=1).astype(int)
        print(" ".join(f"{val:3}" for val in vals))
    if h > max_display or w > max_display:
        print("...")

# Função principal:
def main():
    print(r"Exemplo de caminho: C:\Users\usuario\OneDrive\Desktop\logo_gimp.jpg" '\n')
    caminho = input("Digite o caminho da imagem (ou ENTER para sair): ")
    if not caminho:
        print("Encerrando.")
    try:
        matriz_np, modo = carregar_imagem_para_matriz(caminho, mode='L')
    except Exception as e:
        print(f"Erro ao carregar a imagem: {e}")
    exibir_matriz(matriz_np)

    while True:
        print("\nEscolha a operação:")
        print("1 - Espelhar vertical")
        print("2 - Espelhar horizontal")
        print("3 - Girar 90º horário")
        print("4 - Girar 180º")
        print("5 - Girar 90º anti-horário")
        op = input("Opção (1-5): ")

        # Escolhas de manipulação matricial para o usuário:
        lista = matriz_np.tolist()
        if op == '1':
            lista = espelhar_vertical(lista)
        elif op == '2':
            lista = espelhar_horizontal(lista)
        elif op == '3':
            lista = girar_90(lista)
        elif op == '4':
            lista = girar_180(lista)
        elif op == '5':
            lista = girar_menos_90(lista)
        else:
            print("Opção inválida ou sair.")
            print(r"Exemplo de caminho: C:\Users\usuario\OneDrive\Desktop\nova_imagem")
            saida = input("Digite o caminho para salvar a imagem resultante: ")
            if saida:
                try:
                    salvar_matriz_como_imagem(matriz_np, modo, saida)
                    print(f"Imagem salva em {os.path.abspath(saida)}\n")
                except Exception as e:
                    print(f"Erro ao salvar: {e}\n")
            break
        
        matriz_np = np.array(lista)
        exibir_matriz(matriz_np)

main()

