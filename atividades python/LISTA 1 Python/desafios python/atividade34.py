B = float(input("Base Maior: "))
b = float(input("Base Menor: "))
h = float(input("Altura: "))

if B > b:
    print(f"Área: {((B + b) * h) / 2}")
else:
    print("A base maior deve ser maior que a base menor.")
lado = float(input("Digite o valor do lado: "))

area = lado * lado

print(f"A área do quadrado é: {area}")
