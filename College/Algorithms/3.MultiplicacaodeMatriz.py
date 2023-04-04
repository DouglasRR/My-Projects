# Definição das dimensões das matrizes
linha_matriz_a = int(input("Digite a quantidade de linhas da matriz A: "))
coluna_matriz_a = int(input("Digite a quantidade de elementos de cada linha A: "))
linha_matriz_b = int(input("\nDigite a quantidade de linhas da matriz B: "))
coluna_matriz_b = int(input("Digite a quantidade de elementos de cada linha B: "))

# Condicional para realizar a multiplicação.
if coluna_matriz_a == linha_matriz_b:

    # Criação da Matriz A
    matriz_a = []
    print("\n")
    for contador_linha_a in range(linha_matriz_a):
        linha_a = []
        for contador_coluna_a_a in range(coluna_matriz_a):
            elemento_a = int(input("Digite um número para atribuir a matriz A:"))
            linha_a.append(elemento_a)
        matriz_a.append(linha_a)

    # Criação da Matriz B
    matriz_b = []
    print("\n")
    for contador_linha_b in range(linha_matriz_b):
        linha_b = []
        for contador_coluna_b in range(coluna_matriz_b):
            elemento_b = int(input("Digite um número para atribuir a matriz B:"))
            linha_b.append(elemento_b)
        matriz_b.append(linha_b)

    # Apresentação da Matriz A
    print(f"Matriz A - Dimensão ({linha_matriz_a}x{coluna_matriz_a})")
    for aux1 in range(linha_matriz_a):
        print(matriz_a[aux1])

    # Apresentação da Matriz B
    print(f"\nMatriz B - Dimensão ({linha_matriz_b}x{coluna_matriz_b})")
    for aux2 in range(linha_matriz_b):
        print(matriz_b[aux2])

    # Definição das dimensões e Criação da matriz C
    linha_matriz_c = linha_matriz_a
    coluna_matriz_c = coluna_matriz_b
    auxc1 = linha_matriz_b
    matriz_c = []
    for contador_linha_c in range(linha_matriz_c):
        linha_c = []
        elemento_c = 0
        for contador_coluna_c in range(coluna_matriz_c):
            auxc2 = 0
            for auxc2 in range(auxc1):
                elemento_c += matriz_a[contador_linha_c][auxc2] * matriz_b[auxc2][contador_coluna_c]
            linha_c.append(elemento_c)
        matriz_c.append(linha_c)

    # Apresentação da Multiplicação das Matrizes(matriz C)
    print(f"\n(Multiplicação) Matriz C - ({linha_matriz_c}x{coluna_matriz_c})")
    for aux3 in range(linha_matriz_c):
        print(matriz_c[aux3])
else:
    # Caso a soma não seja possível
    print(f"\nA MULTIPLICAÇÃO NÃO É POSSÍVEL!")
