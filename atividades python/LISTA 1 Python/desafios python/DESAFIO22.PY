moedas_1_centavos =int(input("digite a quantidade de moedas de 1 centavos"))
moedas_5_centavos =int(input("digite a quantidade de moedas de 5 centavos"))
moedas_10_centavos =int(input("digite a quantidade de moedas de 10 centavos"))
moedas_25_centavos =int(input("digite a quantidade de moedas de 25 centavos"))
moedas_50_centavos =int(input("digite a quantidade de moedas de 50 centavos"))
moedas_1_real =int(input("digite a quantidade de moedas de 1 real"))

totais_reais= (moedas_1_centavos * 0.01) + (moedas_5_centavos * 0.05) + (moedas_10_centavos * 0.10) + \
      (moedas_25_centavos * 0.25) + (moedas_50_centavos * 0.50) + (moedas_1_real * 1.00)

print("o valor total em reais e:",totais_reais)