total=float(input("digite o valor total da conta: "))

valor_por_pessoa = total / 3

carlos=int(valor_por_pessoa)
andre=int(valor_por_pessoa)

felipe=total-(carlos+andre)

print("carlos deve pagar R$ {:2f}", format (carlos))
print("andré deve pagar R$ {:2f}", format (andre))
print("felipe deve pagar R$ {:2f}", format (felipe))
