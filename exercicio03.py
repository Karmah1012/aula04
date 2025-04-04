hora1 = int(input("Digite um horario: "))
minuto1 = int(input("Digite a quantidade de minutos"))
hora2 = int(input("Digite um horario: "))
minuto2 = int(input("Quantos minutos?"))
###################################################
somahora = hora1 + hora2
somaminuto = minuto1 + minuto2
##################################################
if somahora >= 24 :
    somahora = somahora - 24
##################################################
if somaminuto >= 60 :
    somahora = somahora -12
    somahora = somahora +1
    somaminuto = somaminuto -60
print(f"O horário foi: {somahora}:{somaminuto}")








