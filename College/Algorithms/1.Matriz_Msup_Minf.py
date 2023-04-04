# Criando a matriz quadrática
tamanho_matriz = int(input("Defina o tamanho da matriz: "))
matriz_a = []

# Adicionando elementos na Matriz
for contador_coluna in range(tamanho_matriz):
    linha = []
    for contador_linha in range(tamanho_matriz):
        elemento = int(input("Digite um número para adicionar a matriz: "))
        linha.append(elemento)
    matriz_a.append(linha)
print("\nMATRIZ DIGITADA PELO USUÁRIO:")
for contador_print in range(tamanho_matriz):
  print(matriz_a[contador_print])

# Criando uma 2ª matriz para receber a matriz superior
print("MATRIZ SUPERIOR: ")
matriz_b = []
for aux1 in range(tamanho_matriz):
    linha_matriz_b = []
    for aux2 in range(tamanho_matriz):
        if aux2 > aux1 - 1:
            linha_matriz_b.append(matriz_a[aux1][aux2])
        else:
            linha_matriz_b.append(0)
    matriz_b.append(linha_matriz_b)
for cont_aux1 in range(tamanho_matriz):
  print(matriz_b[cont_aux1])

# Criando uma 2ª matriz para receber a matriz inferior
print("MATRIZ INFERIOR: ")
matriz_c = []
for aux3 in range(tamanho_matriz):
    linha_matriz_c = []
    for aux4 in range(tamanho_matriz):
        if aux3 > aux4 - 1:
            linha_matriz_c.append(matriz_a[aux3][aux4])
        else:
            linha_matriz_c.append(0)
    matriz_c.append(linha_matriz_c)
for cont_aux2 in range(tamanho_matriz):
    print(matriz_c[cont_aux2])
