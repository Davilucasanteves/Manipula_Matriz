# instale a biblioteca Pillow com: pip install pillow
# instale a biblioteca numpy com: pip install numpy
from PIL import Image
import numpy as np
import os

# Operações matriciais adaptadas para qualquer dimensão e canais:
def espelhar_vertical(matriz):
    rows = len(matriz)
    cols = len(matriz[0])
    nova = [[None]*cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            nova[i][j] = matriz[rows - 1 - i][j]
            # Inverte a ordem das linhas(que equivale a inverter os elementos das colunas), como se virasse a imagem “de cabeça para baixo”;
            # Isso através da operação "n-1-i";;
            # Exemplo: ordem35 - 1 - linha 0 = 34. Isto é, linha 0 vira linha 34, ou seja, a primeira linha vira a última;
    return nova

def espelhar_horizontal(matriz):
    rows = len(matriz)
    cols = len(matriz[0])
    nova = [[None]*cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            nova[i][j] = matriz[i][cols - 1 - j]
            # Inverte a ordem das colunas(que equivale a inverter os elementos das linhas), como se passasse por um espelho;
            # Isso através da operação "n-1-j";
            # O exemplo é equivalente ao anterior, mas com colunas;
    return nova

def girar_90(matriz): 
    rows = len(matriz)
    cols = len(matriz[0])
    nova = [[None]*rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            nova[j][rows - 1 - i] = matriz[i][j]
            # Inverte a ordem das linhas e só depois transpõe-se a matriz;
            # Visualmente é como se a 1º coluna invertesse seus elementos e então se tornasse a 1º linha;
            # Ou seja, a 1º coluna invertida vira a 1º linha;
    return nova

def girar_180(matriz):
    rows = len(matriz)
    cols = len(matriz[0])
    nova = [[None]*cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            nova[rows - 1 - i][cols - 1 - j] = matriz[i][j]
            # Inverte-se tanto a ordem das linhas quanto das colunas, como se a imagem fosse girada em 180º;
            # Ou seja, vira de cabeça para baixo e espelha;
    return nova

def girar_menos_90(matriz):
    rows = len(matriz)
    cols = len(matriz[0])
    nova = [[None]*rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            nova[cols - 1 - j][i] = matriz[i][j]
            # Inverte a ordem das colunas e só depois transpõe-se a matriz;
            # Visualmente é como se a 1º linha invertesse seus elementos e então se tornasse a primeira coluna;
            # Ou seja, a 1º linha invertida torna-se a 1º coluna;
    return nova

# Funções de I/O e exibição:
def carregar_imagem_para_matriz(caminho_imagem, mode='RGB'):
    imagem = Image.open(caminho_imagem).convert(mode)
    matriz = np.array(imagem)
    # converter para lista de listas de pixels:
    if mode == 'RGB':
        return matriz.tolist(), mode
    else:
        return [[int(v) for v in row] for row in matriz], mode


def salvar_matriz_como_imagem(matriz, modo, caminho_saida):
    # Garante extensão válida
    root, ext = os.path.splitext(caminho_saida)
    if ext.lower() not in ['.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.pbm']:
        caminho_saida = f"{caminho_saida}.png"
    arr = np.array(matriz, dtype=np.uint8)
    imagem_resultado = Image.fromarray(arr, mode=modo)
    imagem_resultado.save(caminho_saida)

def exibir_matriz(matriz, max_display=1500):
    rows = len(matriz)
    cols = len(matriz[0])
    print(f"Matriz: {rows}x{cols}")
    for i in range(min(rows, max_display)):
        linha = matriz[i][:min(cols, max_display)]
        # se pixel for tupla RGB, exibe média
        valores = [int(np.mean(p)) if isinstance(p, (list, tuple)) else p for p in linha]
        print(" ".join(f"{v:3}" for v in valores))
    if rows>max_display or cols>max_display:
        print("...")

# Função principal:
def main():
    while True:
        print('------------------------')
        print(r"Exemplo de caminho: C:\Users\usuario\OneDrive\Desktop\logo_gimp.jpg" '\n')
        caminho = input("Caminho da imagem (ENTER sai): ")
        if not caminho:
            break
        try:
            matriz, modo = carregar_imagem_para_matriz(caminho, mode='RGB')
        except Exception as e:
            print(f"Erro no load: {e}")
            continue
        exibir_matriz(matriz)
        print("1- Espelha na VERTICAL 2- Espelha na HORIZONTAL 3- gira 90° 4- gira 180° 5- gira -90°")
        opc = input("Opção: ")
        funcs = {'1': espelhar_vertical,'2': espelhar_horizontal,'3': girar_90,'4': girar_180,'5': girar_menos_90}
        if opc not in funcs:
            print("Saiu")
            continue
        matriz = funcs[opc](matriz)
        exibir_matriz(matriz)
        print(r"Exemplo de caminho: C:\Users\usuario\OneDrive\Desktop\nova_imagem")
        out = input("Salvar em: ")
        if out:
            try:
                salvar_matriz_como_imagem(matriz, modo, out)
                print(f"Salvo: {os.path.abspath(out)}")
            except Exception as e:
                print(f"Erro salvar: {e}")

if __name__ == "__main__":
    main()
