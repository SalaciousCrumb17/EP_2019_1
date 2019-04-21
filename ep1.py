# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Lucas Ohara, lucasso1@al.insper.edu.br
# - aluno B: Alexandre GOnçalves Cury, alexandregc2@al.insper.edu.br
# - aluno C: Samuel

def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "andar professor": "Tomar o elevador para o andar do professor",
                "biblioteca": "Ir para a biblioteca",
                "refeitorio": "Ir para o refeitorio",
                "quadra": "Ir para a quadra",
                "banheiro" : "Ir para o banheiro"
                
            }
        },
        "andar professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                "professor": "Falar com o professor"
            }
        },
        "professor": {
            "titulo": "O monstro do Python",
            "descricao": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma.",
            "opcoes": {}
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada"
            }
        },
        "refeitorio": {
            "titulo": "Estábulo do Ponei Saltitante",
            "descricao": "Voce esta norefeitorio",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada",
                "ovo": "coletar o ovo do dragao"
            }
        },
        "quadra": {
            "titulo": "O coliseu do desafio",
            "descricao": "Voce esta na quadra",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada",
                "jogo": "desafiar o gigante apra um duelo"
            }
        },
        "banheiro": {
            "titulo": "O banheiro",
            "descricao": "Voce esta no banheiro",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada",
                "papel": "coletar o papirus higienico"
            }
        }
    }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual



def main():
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()
    
    bolsa = []
    
    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]
        


        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:
            print("Escolha sua opção: ")
            opcoes= (cenarios[nome_cenario_atual]["opcoes"])
            for lugar, caminho in opcoes.items():
                print("{0}: {1}".format(lugar, caminho))


            escolha=input("Escolha sua opção: ")
            if (escolha == "ovo") or (escolha == "papel"):
                 if escolha not in bolsa:
                    bolsa.append(escolha)
            elif escolha in opcoes:
                nome_cenario_atual = escolha

                
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()


    
    
    
    
    
    
    
    