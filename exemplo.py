docente = {
    "nome": "Mário Gonçalves",
    "idade": 28,
    "diciplina": "POO",
    "turma": "LCC"
}
#Acesso aos valores
print(docente["nome"]) # Mário Gonçalves
print(docente["idade"]) #28
print(docente["diciplina"]) #POO
print(docente["turma"])#LCC
# Adicionar ou Alterar elementos
docente["email"] = "mario@ifbaiano.edu.br" #adicionar
docente["idade"] = 29 # alterar
print(docente)
# Remover elementos
del docente["turma"] #remover o par chave-primaria
idade = docente.pop ("idade")  #remove e retorna o valor
print(idade)  #29 
print(docente)
docente.clear() #remove todos os elementos
print(docente)  #{}

