litrocombustivel = float(input("Quantos litros de combustivel vc colocou? \n"))
combustivel = input("Digite seu combustivel \n"
                    "G para gasolina \n"
                    "E para Etanol \n")
vGas = 5.8
vEta = 4.9

if combustivel == "G" or combustivel == "g":
    valorgasolina = litrocombustivel * vGas
    print(f"Voce abasteceu {litrocombustivel} litros e gastou {valorgasolina} reais")
else:
    if combustivel == "E" or combustivel == "e":
        valoretanol = litrocombustivel * vEta
        print(f"Voce abasteceu {litrocombustivel} e gastou {valoretanol} reais")







