litrocombustivel = float(input("Quantos litros de combustivel vc colocou? \n"))
combustivel = input("Digite seu combustivel \n"
                    "G para gasolina \n"
                    "E para Etanol \n")
vGas = 5.8
vEta = 4.9

if combustivel == "G":
    valorgasolina = litrocombustivel * vGas
    print(f"Voce abasteceu {litrocombustivel} e gastou {valorgasolina} de gasolina")
else:
    if combustivel == "E":
        valoretanol = litrocombustivel * vEta
        print(f"Voce abasteceu {litrocombustivel} e gastou {valoretanol} de etanol")







