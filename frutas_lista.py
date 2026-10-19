frutas = ["Maçã", "Banana", "Uva", "Laranja"]
novo_item = input("Informe o nome da fruta para adicionar na lista: "). strip().title()
frutas.append(novo_item)
print(frutas)
continuar = "sim"
while continuar == "sim":
    frutas = ["Maçã", "Banana", "Uva", "Laranja"]
    novo_item = input("informe o nome da fruta para adicionar na lista: ").strip().title()
    frutas.append(novo_item)
    print(frutas)
    continuar = input("Deseja continuar: [sim ou não]")