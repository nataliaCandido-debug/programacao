estoque_maca=71
min_estoque_maca=25

estoque_melancia=67
min_estoque_melancia=29

estoque_uva=93
min_estoque_uva=13

estoque_mamao=63
min_estoque_mamao=10

estoque_leite=77
min_estoque_leite=27

estoque_macarrao=84
min_estoque_macarrao=4

estoque_bolacha=59
min_estoque_bolacha=11

estoque_sabonete=66
min_estoque_sabonete=17

bolacha = {
    'estoque_maximo':200,
    'estoque_minimo':10,
}

uva = {
    'estoque_maximo':150,
   'estoque_minimo':17,
}

macarrao = {
    'estoque_maximo':123,
    'estoque_minimo':13,
}

sabonete = {
    'estoque_maximo':107,
    'estoque_minimo':34,
}

mamao = {
    'estoque_maximo':337,
    'estoque_minimo':11,
}

maca = {
    'estoque_maximo':201,
    'estoque_minimo':27,
}

melancia = { 
    'estoque_maximo':437,
    'estoque_minimo':17,
}

leite = {
    'estoque_maximo':357,
    'estoque_minimo':23,
}

if estoque < estoque_minimo:
    print ("favor de repor o estoque!Está abaixo do esperado.")
elif estoque > estoque_maximo:
    print ("o esoque està mais cheio do que o esperado!Favor retirar.")
else :
    ("estoque está conforme o esperado!Não precisa mudar.")
