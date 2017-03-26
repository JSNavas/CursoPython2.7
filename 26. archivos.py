archivo = open ("fondos.txt", "w")

archivo.write(raw_input("Escriba aqui: ") + "\n")


archivo.close()

archivo = open ("fondos.txt", "r")

print archivo.read(100)

raw_input()

