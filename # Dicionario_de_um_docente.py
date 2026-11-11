# Dicionario de um docente
docente = {
    "nome": "Mário Gonçalves",
    "Telefone": "(74)91454-0001",
    "idade": 28,
    "diciplina": "Programção Orientada a Objetos",
    "turma": "LCC"
}
# Memsagem com os nomes das diciplinas
print(f"O prfessor {docente['nome']} ministra a diciplina de {docente['diciplina']}.")

#lista com quantro docentes
docentes_if = [


    {
        "nome": "Mário Gonçalves",
        "telefone": "(74)91456-0001",
        "idade": 28,
        "disciplina": "Programação Orientada a Objetos",
        "turma": "LCC"
    },
    {
        "nome": "Mário Pierre",
        "telefone": "(74) 91567-0002",
        "idade": 35,
        "disciplina": "Banco de Dados",
        "turma": "LCC"
    },
    {
        "nome": "Jesse Nery",
        "telefone": "(74) 91245-0003",
        "idade": 32,
        "disciplina": "Estruturas de Dados",
        "turma": "LCC"
    },
    {
        "nome": "Diego Conceição",
        "telefone": "(74) 91985-0004",
        "idade": 30,
        "disciplina": "Programação Web",
        "turma": "LCC"
    }
]


# Segundo docente da lista (índice 1)
segundo = docentes_if[1]
print(f"\nSegundo docente: {segundo['nome']} - {segundo['disciplina']}\n")
# Percorrer a lista toda
for docente in docentes_if:
    for chave, valor in docente.items():
           print(f"{chave}:{valor}")
