import json

# tentar carregar jogadores do arquivo

try:
    with open('jogadores.json', 'r') as arquivo:
        registro_jogadores = json.load(arquivo)
except FileNotFoundError:
    registro_jogadores = []

def menu():
    print("\n" + "="*60)
    print("🏀                MINI ESPN                🏀")
    print("="*60)

    print("\nEscolha uma opção:\n")

    print("[1] Registrar jogador")
    print("[2] Registrar jogo")
    print("[3] Ver estatísticas de jogador")
    print("[4] Ver líder de pontuação")
    print("[5] Buscar jogador")
    print("[6] Buscar jogo")
    print("[7] Sair")

    print("\n" + "="*60)

while True:
    try:
        menu()
        pergunta = int(input("Digite o número da opção desejada: "))
        print("-"*60)

        # sair do programa
        if pergunta == 7:
            print("\n❤️ Obrigado por utilizar o MINI ESPN! ❤️")
            print("-"*60)
            break

        # registrar jogador
        elif pergunta == 1:
            print("\n🏀 REGISTRO DE JOGADOR")
            print("-"*60)

            nome = input("Nome do jogador: ")
            pontos = int(input("Pontos marcados: "))
            assistencias = int(input("Assistências: "))
            rebotes = int(input("Rebotes: "))

            jogador = {
            'nome': nome,
            'pontos': pontos,
            'assistencias': assistencias,
            'rebotes': rebotes
            }

            registro_jogadores.append(jogador)

            with open('jogadores.json', 'w') as arquivo:
                json.dump(registro_jogadores, arquivo, indent=4)

            print("\n✅ Jogador registrado com sucesso!")
            print("-"*60)

            ver_lista = input("Deseja ver a lista de jogadores? (sim/não): ").lower().replace(" ", "")

            if ver_lista == 'sim':
                print("\n📋 JOGADORES REGISTRADOS")
                print("-"*60)

                for j in registro_jogadores:
                    print("•", j['nome'])

        # registrar jogo
        elif pergunta == 2:

            try:
                with open('jogos.json', 'r') as arquivo:
                    registrar_jogo = json.load(arquivo)
            except FileNotFoundError:
                registrar_jogo = []

            print("\n🏀 REGISTRO DE PARTIDA")
            print("-"*60)

            time_casa = input("Time da casa: ")
            time_visitante = input("Time visitante: ")

            pontos_casa = int(input(f"Pontos do {time_casa}: "))
            pontos_visitante = int(input(f"Pontos do {time_visitante}: "))

            jogo = {
            'time_casa': time_casa,
            'time_visitante': time_visitante,
            'pontos_casa': pontos_casa,
            'pontos_visitante': pontos_visitante
            }

            registrar_jogo.append(jogo)

            with open('jogos.json', 'w') as arquivo:
                json.dump(registrar_jogo, arquivo, indent=4)

            print("\n✅ Partida registrada com sucesso!")
            print("-"*60)

            ver_lista_de_jogos = input("Deseja ver a lista de jogos? (sim/não): ").lower()

            if ver_lista_de_jogos == 'sim':
                print("\n📋 JOGOS REGISTRADOS")
                print("-"*60)

                for l in registrar_jogo:
                    print(l['time_casa'], l['pontos_casa'], "vs", l['time_visitante'], l['pontos_visitante'])

        # ver estatísticas
        elif pergunta == 3:
            print("\n📊 ESTATÍSTICAS DO JOGADOR")
            print("-"*60)

            escolha_do_jogador = input("Digite o nome do jogador: ")

            for n in registro_jogadores:
                if n['nome'] == escolha_do_jogador:
                    print("\n🏀 Dados do jogador")
                    print("-"*60)

                    print(f"Nome: {n['nome']}")
                    print(f"Pontos: {n['pontos']}")
                    print(f"Assistências: {n['assistencias']}")
                    print(f"Rebotes: {n['rebotes']}")

        # ranking
        elif pergunta == 4:

            print("\n👑 LÍDER DE PONTUAÇÃO")
            print("-"*60)

            if len(registro_jogadores) == 0:
                print("Nenhum jogador registrado.")
            else:
                maior = registro_jogadores[0]

                for j in registro_jogadores:
                    if j['pontos'] > maior['pontos']:
                        maior = j

                print(f"\n🏀 Jogador líder: {maior['nome']}")
                print(f"👑 Pontos: {maior['pontos']}")

            print("-"*60)

        # buscar jogador
        elif pergunta == 5:
            print("\n🔎 BUSCAR JOGADOR")
            print("-"*60)

            pesquisa = input("Digite o nome do jogador: ").strip().lower()

            for j in registro_jogadores:
                if j['nome'].lower() == pesquisa:

                    print("\n🏀 JOGADOR ENCONTRADO")
                    print("-"*60)

                    print(f"Nome: {j['nome']}")
                    print(f"Pontos: {j['pontos']}")
                    print(f"Assistências: {j['assistencias']}")
                    print(f"Rebotes: {j['rebotes']}")

        # buscar jogo
        elif pergunta == 6:
            try:
                with open('jogos.json', 'r') as arquivo:
                    registrar_jogo = json.load(arquivo)
            except FileNotFoundError:
                registrar_jogo = []

            print("\n🔎 BUSCAR PARTIDA")
            print("-"*60)

            descobrindo_jogo = input("Digite o nome de um dos times: ").strip().lower()

            encontrado = False

            for j in registrar_jogo:

                if j['time_casa'].strip().lower() == descobrindo_jogo or j['time_visitante'].strip().lower() == descobrindo_jogo:
                    encontrado = True

                    print("\n🏀 RESULTADO DA PARTIDA")
                    print("-"*60)

                    if j['pontos_casa'] > j['pontos_visitante']:
                        print(f"{j['time_casa']} 🏆 venceu 🏆 {j['time_visitante']}")
                        print(f"Placar: {j['pontos_casa']} x {j['pontos_visitante']}")

                    elif j['pontos_casa'] < j['pontos_visitante']:
                        print(f"{j['time_visitante']} 🏆 venceu 🏆 {j['time_casa']}")
                        print(f"Placar: {j['pontos_visitante']} x {j['pontos_casa']}")

                    else:
                        print("O jogo terminou empatado!")

            if not encontrado:
                print("\n❌ Time não encontrado. Verifique o nome digitado.")
                    


    except ValueError:
        print("\n🚨 Erro: digite apenas números nas opções do menu!")
