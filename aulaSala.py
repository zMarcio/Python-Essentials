sala1 = ['Erik','Maia','Gustavo','Manuel','Sofia','Joana']
sala2 = ['Joao','Antonio','Carlos', 'Maria','Isolda']

aula_ingles = ['Erik', 'Maia', 'Joana', 'Carlos', 'Antonio']
aula_musica = ['Erik','Carlos','Maria']
aula_danca = ['Gustavo','Sofia','Joana','Antonio']

atividades = {
    "Inglês":aula_ingles,
    "Música": aula_musica, 
    "Dança": aula_danca
}

for nome_Atividade,alunos in atividades.items():
    atividade_sala1 = []
    atividade_sala2 = []
    for aluno in alunos          :    
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)

    print(f"A {nome_Atividade} sala 1 : {atividade_sala1}")
    print(f"A {nome_Atividade} sala 2 : {atividade_sala2}")
    print("-"*50)
