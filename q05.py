repeticoes = int(input("Insira todos os numero: "))
numero = []

for i in range (repeticoes):
    numero.append(int(input(f"Informe o valor {i + 1}: ")))

soma = sum(numero)
media = soma/repeticoes
maior = max(numero)
menor = min(numero)

print(f"a soma é {soma}")
print(f"A média é {media}")
print(f"O maior é {maior}")
print(f"O menor valor é {menor}")

contador = 0
for o in numero:
    if o > media:
        contador += 1
print(f"a quantidade de valores acima da média é {contador}")