numero = int(input("Insira um número inteiro:"))
s = 0

for i in range (1, numero):
    if numero % i == 0:
        s += i

if s == numero:
    print(f"{numero} é perfeito")
else:
    print(f"{numero} não é perfeito")