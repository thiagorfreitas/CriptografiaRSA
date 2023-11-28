print("Decifre uma criptografia RSA")
x = input("Digite os números separados por espaço: ").split()
y = int(input("Digite o valor de B (beta): "))
z = int(input("Digite o valor de N: "))
# Criando um dicionário de acordo com a tabela utilizada de conversão de números para caracteres
dic_letras = {i: chr(i - 10 + ord('A')) for i in range(10, 36)}#{chr(i): i - ord('A') + 10 for i in range(ord('A'), ord('Z') + 1)}
dic_letras[36] = ' '

# List comprehension para converter elementos para inteiros e calcular resultados
results = [str(int(num) ** y % z) for num in x]

# Combinando os resultados em uma única string
res = ' '.join(results)
s = ''.join(results)
# Separando os resultados em pares de dois caracteres
res_splitted = ' '.join([s[i:i+2] for i in range(0, len(s), 2)])
letra = []
print("Resultados:", res)
print("Resultados Agrupados:", res_splitted)
# Decodificando a palavra
for i in range(0, len(res_splitted.split())):
    key = int(res_splitted.split()[i])
    letra.append(dic_letras.get(key, 'Chave nao encontrada'))

palavra = ''.join(letra)
print("Palavra decodificada:", palavra)