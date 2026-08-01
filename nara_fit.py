def validar_valores(pergunta, tipo): # Função auxíliar para não repetir a validação
    while True:
        try:
            valor = tipo(input(pergunta))
            if valor < 0:
                print("Digite um valor válido!")
                continue
            print("Valor salvo com sucesso")
            return valor
        except ValueError:
            print("Digite um dado válido!")
            
# Dicionário com valores e sem valores:
cadastrados = {
    "nomes": [],
    "idades": [],
    "pesos": [],
    "alturas": [],
    "imc": [],
    "status": []
}
# Dicionario com valores predefinidos para testes rapidos: 
'''cadastrados = {
    "nomes": [
        "Special Week",        # Uma Musume
        "Rukia Kuchiki",       # Bleach
        "Emilia",              # Re:Zero
        "Gold Ship",           # Uma Musume
        "Yoruichi Shihoin",    # Bleach
        "Rem",                 # Re:Zero
        "Ichigo Kurosaki",     # Bleach
        "Subaru Natsuki",      # Re:Zero
        "Izuku Midoriya",      # Boku no Hero Academia
        "All Might"            # Boku no Hero Academia
    ],
    "idades": [
        17,    # Special Week (Idade escolar aproximada)
        150,   # Rukia Kuchiki (Aparência jovem, idade de Shinigami)
        114,   # Emilia (Idade real em anos de Meio-Elfo)
        17,    # Gold Ship (Idade escolar aproximada)
        300,   # Yoruichi Shihoin (Estimativa de Shinigami)
        19,    # Rem (Arco 4+)
        17,    # Ichigo Kurosaki (Pós-timeskip)
        18,    # Subaru Natsuki (Arco 5+)
        16,    # Izuku Midoriya 
        49     # All Might 
    ],
    "pesos": [
        46.0,  # Special Week 
        33.0,  # Rukia Kuchiki 
        50.0,  # Emilia 
        51.0,  # Gold Ship 
        42.0,  # Yoruichi Shihoin 
        47.0,  # Rem 
        66.0,  # Ichigo Kurosaki 
        70.0,  # Subaru Natsuki 
        60.0,  # Izuku Midoriya 
        255.0  # All Might ( Forma Musculosa)
    ],
    "alturas": [
        1.55,  # Special Week (m)
        1.44,  # Rukia Kuchiki (m)
        1.64,  # Emilia (m)
        1.70,  # Gold Ship (m)
        1.56,  # Yoruichi Shihoin (m)
        1.54,  # Rem (m)
        1.74,  # Ichigo Kurosaki (m)
        1.73,  # Subaru Natsuki (m)
        1.66,  # Izuku Midoriya (m)
        2.20   # All Might (m)
    ],
    "imc": [
        19.15, # Special Week
        15.91, # Rukia Kuchiki
        18.59, # Emilia
        17.65, # Gold Ship
        17.26, # Yoruichi Shihoin
        19.82, # Rem
        21.80, # Ichigo Kurosaki
        23.39, # Subaru Natsuki
        21.77, # Izuku Midoriya
        52.69  # All Might (Forma Musculosa)
    ],
    "status": [
        "Peso Normal",     # Special Week
        "Abaixo do peso",  # Rukia Kuchiki
        "Peso Normal",     # Emilia
        "Abaixo do peso",  # Gold Ship
        "Abaixo do peso",  # Yoruichi Shihoin
        "Peso Normal",     # Rem
        "Peso Normal",     # Ichigo Kurosaki
        "Peso Normal",     # Subaru Natsuki
        "Peso Normal",     # Izuku Midoriya
        "Obeso" # All Might 
    ]
}'''

# Cadastro e a função auxiliar para calcular o IMC e avaliar:
def calcular_avaliar(peso , altura, index): 
    imc = peso / (altura**2) 
    if imc >= 30: # Se quiser depois adiciona os graus 
        status = "Obeso"
    elif imc >= 25:
        status = "Sobrepeso"
    elif imc >= 18.5:
        status = "Peso Normal"
    else:
        status = "Abaixo do peso"
    if index is not None: # caso seja uma atualização 
        cadastrados["imc"][index] = imc
        cadastrados["status"][index] = status
    else:
        cadastrados["imc"].append(imc)
        cadastrados["status"].append(status)
def cadastro():
    while True: # Caso o usuário queira adicionar sem parar
        perguntas = [
            "Digite uma idade: ",
            "Digite um peso(Em kilos): ",
            "Digite uma altura(Em metros): "
        ]
        nome = input("Digite o nome desejado: ").title()
        cadastrados["nomes"].append(nome)
        for i in perguntas:
            if perguntas.index(i) == 2:
                altura = validar_valores(i, float)
                cadastrados["alturas"].append(altura)
            elif perguntas.index(i) == 1:
                peso = validar_valores(i, float)
                cadastrados["pesos"].append(peso)
            else:
                idade = validar_valores(i, int)
                cadastrados["idades"].append(idade)
        index = len(cadastrados["nomes"]) - 1
        calcular_avaliar(cadastrados["pesos"][index], cadastrados["alturas"][index], None)
        print(f"Adicionado com sucesso!")
        if input("Deseja adicionar mais(S/N)?: ").lower() != "s": # Fazer tratamento de erros depois
            break
# Listagem de alunos:
def listar_exibir(index):
    if index is not None:
        print(f"{index+1}° - {cadastrados["nomes"][index]} | {cadastrados["idades"][index]} anos | {cadastrados["pesos"][index]}Kg | {cadastrados["alturas"][index]}m | IMC: {round(cadastrados["imc"][index], 2)}Kg/m² | Status: {cadastrados["status"][index]}")
    elif len(cadastrados["nomes"]) == 0:
        print("Sem usuários no sistema! Que tal cadastrar antes de checar a lista ou fazer qualquer operação como deletar ou alterar dados?")
    else:
        print(f"{'='*10} Lista de cadastrados {'='*10}")
        for i in range(len(cadastrados["nomes"])): # Por padrão vou usar o nomes 
            print(f"{i+1}° - {cadastrados["nomes"][i]} | {cadastrados["idades"][i]} anos | {cadastrados["pesos"][i]}Kg | {cadastrados["alturas"][i]}m | IMC: {round(cadastrados["imc"][i], 2)}Kg/m² | Status: {cadastrados["status"][i]}")
        print("="*42)
# Estatísticas completa + menu de estatísticas:
def estatisticas():
    if len(cadastrados["nomes"]) == 0:
        print("Sem usuários no sistema! Que tal cadastrar antes de checar a lista?")
    else:
        # Coleta as informações para exibir as estatísticas antes de apresentar o menu
        media = round(sum(cadastrados["idades"]) / len(cadastrados["idades"]), 2) 
        velho = max(cadastrados["idades"])
        cliente_velho = []
        novo = min(cadastrados["idades"])
        cliente_novo = []
        for i in range(len(cadastrados["nomes"])):
            if cadastrados["idades"][i] == velho:
                cliente_velho.append(cadastrados["nomes"][i])
            if cadastrados["idades"][i] == novo:
                cliente_novo.append(cadastrados["nomes"][i])
        obesos = {
            "clientes": [],
            "quantidade": 0
        }
        sobrepesos = {
            "clientes": [],
            "quantidade": 0
        }
        normais = {
            "clientes": [],
            "quantidade": 0
        }
        abaixos = {
            "clientes": [],
            "quantidade": 0
        }
        for i in range(len(cadastrados["status"])):
            if cadastrados["status"][i] == "Obeso":
                obesos["clientes"].append(cadastrados["nomes"][i])
                obesos["quantidade"] += 1
            elif cadastrados["status"][i] == "Sobrepeso":
                sobrepesos["clientes"].append(cadastrados["nomes"][i])
                sobrepesos["quantidade"] += 1
            elif cadastrados["status"][i] == "Peso Normal":
                normais["clientes"].append(cadastrados["nomes"][i])
                normais["quantidade"] += 1
            else:
                abaixos["clientes"].append(cadastrados["nomes"][i])
                abaixos["quantidade"] += 1
        # Menu de exibição de estatísticas:
        while True:
            print("Qual estatísca deseja verificar?")
            print("1. Idade média, alunos mais novos e alunos mais velhos \n2. Status dos alunos \n0. Sair")
            try:
                opcao = int(input("Escolha um número: "))
                if opcao == 2:
                    print("="*42)
                    if obesos["quantidade"] > 0:
                        print(f"Exite(m) {obesos['quantidade']} obeso(s):")
                        for i in range(len(obesos["clientes"])):
                            print(obesos['clientes'][i])
                    if sobrepesos["quantidade"] > 0:
                        print(20*"=")
                        print(f"Exite(m) {sobrepesos['quantidade']} sobrepeso(s):")
                        for i in range(len(sobrepesos["clientes"])):
                            print(sobrepesos['clientes'][i])
                    if normais["quantidade"] > 0:
                        print(20*"=")
                        print(f"Exite(m) {normais['quantidade']} normal/normais:")
                        for i in range(len(normais["clientes"])):
                            print(normais['clientes'][i])
                    if abaixos["quantidade"] > 0:
                        print(20*"=")
                        print(f"Exite(m) {abaixos['quantidade']} abaixo/abaixos do peso:")
                        for i in range(len(abaixos["clientes"])):
                            print(abaixos['clientes'][i])
                    print("="*42)
                elif opcao == 1:
                    print(f"Média de idades: {media}")
                    print(f"A maior idade é {velho} e o(s) aluno(s) que possuem essa idade são: ")
                    for i in cliente_velho:
                        print(i)
                    print(f"A menor idade é {novo} e o(s) aluno(s) que possuem essa idade são: ")
                    for i in cliente_novo:
                        print(i)
                elif opcao == 0:
                    break
                else:
                    print("Número inválido!")
            except ValueError:
                print("Número inválido!")
def alterar():
    if cadastrados['nomes'] == []:
        return None
    else:
        while True:
            try: 
                aluno = int(input("Digite o número do aluno que deseja alterar: "))
            except ValueError:
                print("Digite um número.")
                continue
            if 0 < aluno <= len(cadastrados["nomes"]):
                print("Aluno selecionado: ")
                index = aluno - 1 # Só pra não repetir o -1 
                listar_exibir(index)
                while True:
                    try:
                        opcao = int(input("O que deseja alterar(1. Nome 2. idade 3. Peso 4. Altura)?: "))
                    except ValueError:
                        print("Digite um número inteiro!")
                        continue
                    if opcao == 1:
                        cadastrados['nomes'][index] = input("Digite o nome atualizado: ").title() # só pra ficar em caps
                    elif opcao == 2:
                        cadastrados['idades'][index] = validar_valores("Digite a idade atualizada: ", int)
                    elif opcao == 3:
                        peso = validar_valores("Digite o peso atualizado: ", float)
                        calcular_avaliar(peso, cadastrados['alturas'][index], index)
                        cadastrados['pesos'][index] = peso
                    elif opcao == 4:
                        altura = validar_valores("Digite a altura atualizada: ", float)
                        calcular_avaliar(cadastrados['pesos'][index], altura, index)  
                        cadastrados['alturas'][index] = altura
                    else:
                        print("Digite um número positivo ou dentro das opções!")
                    break
            else:
                print("Número inválido!")
            break
def deletar():
    if len(cadastrados['nomes']) == 0:
        return None
    else:
        while True:
            try:
                aluno = int(input("Digite o número correspondente ao usuário que você quer deletar?(Digite 0 para sair): "))
                index = aluno - 1
            except:
                print("Digite um número.")
                continue
            if 0 < aluno <= len(cadastrados["nomes"]):
                listar_exibir(index)
                if input(f"Deseja realmente deletar esse aluno(S/N): ").lower() == "s": 
                    for key in cadastrados.keys(): # Deleta o index selecionado de todas as chaves
                        cadastrados[key].pop(index)
                    print("Deletado com sucesso!")
                    break
            elif aluno == 0:
                break
            else:
                print("Opção inválida, o número deve ser inteiro, positivo e deve existir no sistema.")
# Menu Principal:
while True:
    print("1 - Deseja cadastrar um usuário?")
    print("2 - Consultar os usuários e valores?")
    print("3 - Consultar estáticas?")
    print("4 - Alterar dados?")
    print("5 - Deletar?")
    print("0 - Sair")
    try: 
        opcao = int(input("Escolha a opção: "))
    except ValueError:
        print("Digite um número")
        continue
    if opcao == 1:
        cadastro()
    elif opcao == 2:
        listar_exibir(None)
    elif opcao == 3:
        estatisticas()
    elif opcao == 4:
        listar_exibir(None)
        alterar()
    elif opcao == 5:
        listar_exibir(None)
        deletar()
    elif opcao == 0:
        if input("Deseja sair mesmo(S/N)?: ").lower() == "s":
            break
    else:
        print("Número inválido, ou é negativo ou não está no sistema.")