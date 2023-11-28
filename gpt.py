x = input("Digite os números separados por espaço: ").split()
y = int(input("Digite o expoente: "))
z = int(input("Digite o divisor: "))
dic_letras = {i: chr(i - 10 + ord('A')) for i in range(10, 36)}#{chr(i): i - ord('A') + 10 for i in range(ord('A'), ord('Z') + 1)}
dic_letras[36] = ' '

# Use list comprehension para converter elementos para inteiros e calcular resultados
results = [str(int(num) ** y % z) for num in x]

# Combine os resultados em uma única string
res = ' '.join(results)
s = ''.join(results)
# Separe os resultados em pares de dois caracteres
res_splitted = ' '.join([s[i:i+2] for i in range(0, len(s), 2)])
letra = []
print("Resultados:", res)
print("Resultados Agrupados:", res_splitted)
for i in range(0, len(res_splitted.split())):
    key = int(res_splitted.split()[i])
    letra.append(dic_letras.get(key, 'Chave nao encontrada'))

palavra = ''.join(letra)
print("Palavra decodificada:", palavra)