cavaleiros = ["Aiolia", "Shaka", "Mu", "Milo", "Camus"]

print("Quantidade inicial:", len(cavaleiros))
cavaleiros.append("Aiolos")
cavaleiros.insert(0,"Dohko")
cavaleiros.remove("Milo")
romovido = cavaleiros.pop()
print("Cavaleiro Romovido:",romovido)
print("Primeiro da lista:",cavaleiros[0])
cavaleiros.sort()
print("cavaleiros que participarão da batalha:")
for c in cavaleiros:
    print(c)
print("Quantidade de cavaleiros restantes:",len(cavaleiros))