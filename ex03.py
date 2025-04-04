horario1 = int(input("Digite o horário até 12:"))
minuto1 = int(input("Digite o minuto:"))
horario2 = int(input("Digite o horário até 24:"))
minuto2 = int(input("Digite o minuto:"))
###################################################
horasaida = horario1+horario2
minutosaida = minuto1+minuto2
###################################################
if horasaida >= 24 :
    horasaida = horasaida - 24
###################################################
if minutosaida >= 60 :
    horasaida = horasaida - 12
    horasaida = horasaida +1
    minutosaida = minutosaida -60
    print(f"O horário é: {horasaida}:{minutosaida}")