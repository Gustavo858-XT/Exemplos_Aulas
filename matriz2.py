cavaleiros = ["Aiolia", "Shaka", "Mu", "Milo", "Camus"]

print("Quantidade inicial:", len(cavaleiros))
cavaleiros.append("Aiolos")
cavaleiros.insert(0, "Dohko")
cavaleiros.remove("Milo")
removido = cavaleiros.pop()
print("Cavaleiro removido:", removido)
print("Primeiro da lista:", cavaleiros[0])
cavaleiros.sort()

print("Cavaleiros que participarão da batalha:")
print("-" * 22)
print(f"{'Nº':<4}| {'Cavaleiro':<15}")
print("-" * 22)
for i, c in enumerate(cavaleiros, start=1):
    print(f"{i:<4}| {c:<15}")
print("-" * 22)

print("Quantidade de cavaleiros restantes:", len(cavaleiros))