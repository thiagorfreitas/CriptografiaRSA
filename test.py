# Dicionário com a correspondência entre números e letras
numeros_para_letras = {i: chr(i - 10 + ord('A')) for i in range(10, 36)}
numeros_para_letras[0] = ' '  # Adicione o espaço ao dicionário

# Entrada do usuário
x = input("Digite os números separados por espaço: ").split()
y = int(input("Digite o expoente: "))
z = int(input("Digite o divisor: "))

# Use list comprehension para converter elementos para inteiros e calcular resultados
resultados_numeros = [int(num) ** y % z for num in x]

# Use a inversão do dicionário para obter as letras correspondentes aos números
resultados_letras = [numeros_para_letras[num] for num in resultados_numeros]

# Combine os resultados em uma única string
palavra_decodificada = ''.join(resultados_letras)

print("Palavra Decodificada:", palavra_decodificada)
