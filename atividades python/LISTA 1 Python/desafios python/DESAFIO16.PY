Peso_queijo = 50 #gramas
peso_presunto = 50 #gramas
peso_burguer = 100 #gramas

quantidade_sanduiche= int(input("Digite a quantidade de sanduiches: "))
peso_queijo_total = quantidade_sanduiche * (Peso_queijo * 2)
peso_presunto_total = quantidade_sanduiche * peso_presunto
peso_burguer_total = quantidade_sanduiche * peso_burguer

peso_queijo_totalkg = peso_queijo_total/1000
peso_presunto_totalkg = peso_presunto_total/1000
peso_burguer_totalkg = peso_burguer_total/1000

print(f"peso total queijo: {peso_queijo_totalkg:.2f}")
print(f"peso total presunto: {peso_presunto_totalkg:.2f}")
print(f"peso total burguer: {peso_burguer_totalkg:.2f}")
