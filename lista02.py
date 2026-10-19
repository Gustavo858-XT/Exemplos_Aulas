# Inplementando uma lista de frutas
frutas = ["Maçã", "Banana", "Uva", "Laranja"]
#Adicionando onome da feira em uma variável
texto = "ғʀᴜᴛɪғ - A ʀᴇɪᴛᴏʀɪᴀ ᴅᴏ sᴀʙoʀ"
print('='* (len(texto)+6))
print(f" {texto} ")
print('='* (len(texto)+6))
contador = "sim"
while contador == "sim":
    novo_item = input("Digite o nome da fruta para adicionar a feira: ").strip().title()
    if novo_item == '':
        print("Digite o nome de uma fruta para realizar o cadastro: ")
    elif novo_item in frutas:
        posicao = frutas.index(novo_item)
        print(f"O item informado já existe na lista na posição {posicao}")
    else:
        frutas.append(novo_item)
        print(f"A fruta {frutas[-1]} foi cadastada com sucesso")
        print(frutas)
    contador = input("Deseja continuar 'sim' ou 'não': ").strip().lower()
for i, fruta in enumerate(frutas):
    print(frutas)
print(f"A lista contém {len(frutas)} tipos de frutas ")