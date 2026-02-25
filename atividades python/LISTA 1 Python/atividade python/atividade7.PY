h = float(input("digite a altura em centimetros"))

sexo = (input("digite seu sexo(sexo(m ou f))"))
if sexo == "m" :
peso_ideal=(72.7*h) - 58
print("para homens o peso ideal é ",peso ideal)
if sexo == "f" :
peso_ideal=(62.1*h) - 44.7
print("para mulheres o peso ideal é ",peso ideal)
else:
print("sexo invalido")