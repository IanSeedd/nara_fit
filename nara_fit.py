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

cadastrados = {
    "nomes": [],
    "idades": [],
    "pesos": [],
    "alturas": [],
    "imc": [],
    "status": []
}
# Cadastro e a função auxiliar para calcular o IMC e avaliar:
def calcular_avaliar(peso , altura): 
    imc = peso / (altura**2) 
    if imc >= 30: # Se quiser depois adiciona os graus 
        status = "Obeso"
    elif imc >= 25:
        status = "Sobrepeso"
    elif imc >= 18.5:
        status = "Peso Normal"
    else:
        status = "Abaixo do peso"
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
        calcular_avaliar(cadastrados["pesos"][index], cadastrados["alturas"][index])
        print(f"Adicionado com sucesso!")
        if input("Deseja adicionar mais(S/N)?: ").lower() != "s": # Fazer tratamento de erros depois
            break
# Listagem de alunos:
def listar():
    if len(cadastrados["nomes"]) == 0:
        print("Sem usuários no sistema! Que tal cadastrar antes de checar a lista?")
    else:
        print(f"{"="*10} Lista de cadastrados {"="*10}")
        for i in range(len(cadastrados["nomes"])): # Por padrão vou usar o nomes 
            print(f"{i+1}° - {cadastrados["nomes"][i]} | {cadastrados["idades"][i]} anos | {cadastrados["pesos"][i]}Kg | {cadastrados["alturas"][i]}cm | IMC: {round(cadastrados["imc"][i], 2)}Kg/m² | Status: {cadastrados["status"][i]}")
        print(f"{"="*42}")
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
            elif cadastrados["idades"][i] == novo:
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
                    print(f"{"="*42}")
                    if obesos["quantidade"] > 0:
                        print(f"Exite(m) {obesos['quantidade']} obeso(s):")
                        for i in range(len(obesos["clientes"])):
                            print(obesos['clientes'][i])
                    if sobrepesos["quantidade"] > 0:
                        print(f"Exite(m) {sobrepesos['quantidade']} sobrepeso(s):")
                        for i in range(len(sobrepesos["clientes"])):
                            print(sobrepesos['clientes'][i])
                    if normais["quantidade"] > 0:
                        print(f"Exite(m) {normais['quantidade']} normal/normais:")
                        for i in range(len(normais["clientes"])):
                            print(normais['clientes'][i])
                    if abaixos["quantidade"] > 0:
                        print(f"Exite(m) {abaixos['quantidade']} abaixo/abaixos do peso:")
                        for i in range(len(abaixos["clientes"])):
                            print(abaixos['clientes'][i])
                    print(f"{"="*42}")
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

# Menu Principal:
while True:
    print("1 - Deseja cadastrar um usuário?")
    print("2 - Consultar os usuários e valores?")
    print("3 - Consultar estáticas?")
    print("4 - Sair")
    try: 
        opcao = int(input("Escolha a opção: "))
    except ValueError:
        print("Digite um número")
    if opcao == 1:
        cadastro()
    elif opcao == 2:
        listar()
    elif opcao == 3:
        estatisticas()
    elif opcao == 4:
        if input("Deseja sair mesmo(S/N)?: ").lower() == "s":
            break
    else:
        print("Número inválido.")