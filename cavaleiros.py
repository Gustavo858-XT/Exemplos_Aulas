cavaleiros = [
[1, "Capricórnio", "Shura"],
[2, "Aquário", "Camus"],
[3, "Peixes", "Afrodite"],
[4, "Áries", "Mu"],
[5, "Touro", "Aldebaran"],
[6, "Gêmeos", "Saga / Kanon"],
[7, "Câncer", "Máscara da Morte"],
[8, "Leão", "Aiolia"],[9, "Virgem", "Shaka"],
[10, "Libra", "Dohko"],
[11, "Escorpião", "Milo"],
[12, "Sagitário", "Aiolos"]
]

mes = int(input("Digite seu mês de nascimento: "))
if mes not in cavaleiros:
    print(f"Seu cavaleiro de ouro é: {cavaleiros[mes-1][2]} de {cavaleiros[mes-1][1]}")
else:
    print("Mês invalido, digite o nome do mês")