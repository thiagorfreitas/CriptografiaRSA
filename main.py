x = input().split()
y = int(input())
z = int(input())

res = ""
for i in range(0, len(x)):
    x[i] = int(x[i])
    tmp = x[i] ** y
    curr_res = tmp % z
    res = res + str(curr_res)

res_splitted = ""
for i in range(0, len(res), 2):
    res_splitted = res_splitted + res[i:i + 2] + " "

print(res)
print(res_splitted)
