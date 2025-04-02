hora1 = int(input("Digite um horario ate 12h: "))
minuto1 = float(input("Digite a quantidade de minutos"))
hora2 = int(input("Digite um horario ate 24h"))
minuto2 = float(input("Quantos minutos?"))
###################################################
somahora = (hora1 + hora2)
somaminuto = (minuto1 + minuto2)
somatotal = (somahora + somaminuto) /12
##################################################
if somahora > 12 :
    somahora = (- 12 + somatotal)
##################################################
if somaminuto >= 60 :
    somaminuto = (-60 + somaminuto)
print(f"São: {somatotal} ")



