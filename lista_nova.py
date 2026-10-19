frutas = ["Maçã", "Banana", "Uva", "Laranja"]
frutas [0]
frutas [2]
frutas [-1]
# Alterando Elemento
frutas [1] = "Abacaxi"
# Inserindo Elemento
frutas.append("Melancia")
frutas.insert(1, "Pera")
frutas.extend(["Kiwi", "Manga"])
# Acessando os Elementos
print(frutas [0])
print(frutas [2])
print(frutas [-1])
print("Inprimindo todos os elementos\n")
for frutas in frutas:
    print(frutas)
