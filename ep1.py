# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Lucas Ohara, lucasso1@al.insper.edu.br
# - aluno B: Alexandre GOnçalves Cury, alexandregc2@al.insper.edu.br
# - aluno C: Samuel




import random

def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "monstro":0,
            "hit": 0,
            "coins":0,
            "opcoes": {
                "andar professor": "Tomar o elevador para o andar do professor",
                "biblioteca": "Ir para a biblioteca",
                "refeitorio": "Ir para o refeitorio",
                "quadra": "Ir para a quadra",
                "banheiro" : "Ir para o banheiro",
<<<<<<< HEAD
                "estacionamento": "Ir para o estacionamento"
=======
<<<<<<< HEAD
                "Estacionamento": "Ir para o estacionamento"
=======
                "teleporte": "Ir para a sala de teleporte"
>>>>>>> 88a0974bf238f76a61c9f1f5f2151ea32ad9ac72
>>>>>>> 8540eb165a1ec1853de1a26222393714a8924461
                
            }
        },
        "andar professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "monstro": "veterano",
            "hit": 10,
            "coins":10,
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                "professor": "Falar com o professor",
                },
        },
        "professor": {
            "titulo": "O monstro do Python",
            "monstro":0,
            "hit":0,
            "coins":0,
            "descricao": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma.",
            "opcoes": {},
            
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "monstro": "veterano",
            "hit": 10,
            "coins":10,
            "opcoes": {

                "inicio": "Voltar para o saguao de entrada",
                "livro": "pegar a cronica de dor e gloria"
            }

        },
        "refeitorio": {
            "titulo": "Estábulo do Ponei Saltitante",
            "descricao": "Voce esta no refeitorio",
            "monstro": "veterano",
            "hit": 10,
            "coins":10,

            "opcoes": {
                "inicio": "Voltar para o saguao de entrada",
                "ovo": "coletar o ovo do dragao"
                }
        },
        "quadra": {
            "titulo": "O coliseu do desafio",
            "monstro": "veterano",
            "hit": 10,
            "coins":10,
            "descricao": "Voce esta na quadra",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada",
                "bola": "obter a bola do gigante da cesta"
                }
                
        },
        "banheiro": {
            "titulo": "O banheiro",
            "descricao": "Voce esta no banheiro",
            "monstro": "veterano",
            "hit": 10,
            "coins":10,
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada",
                "papel": "coletar o papirus higienico"
                }
<<<<<<< HEAD

        
=======
<<<<<<< HEAD
        
        },
        "Estacionamento": {
                "titulo": "A Sala de Teleporte",
                "descricao": "Diga o nome de onde voce quer ir",
                "monstro": "veterano",
                "hit": 10,
                "coins":10,
                "opcoes": {
                        "teleporte": "Teleportar para qualquer sala",
                        "inicio": "Retornar ao Inicio"
                       
                        }
                }
=======
>>>>>>> 8540eb165a1ec1853de1a26222393714a8924461
        },
        "estacionamento": {
                "titulo": "s sala de teleporte",
                "descricao": "diga o nome de onde voce quer ir",
                "monstro": "veterano",
                "hit": 10,
                "coins":10,
                "opcoes": {
                        "teleporte": "teleportar para qualquer sala",
                        "inicio": "retornar ao Inicio"
                       
                        }
                }
        }
<<<<<<< HEAD

=======
>>>>>>> 88a0974bf238f76a61c9f1f5f2151ea32ad9ac72
    }
>>>>>>> 8540eb165a1ec1853de1a26222393714a8924461
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
    life= 100
    moeda=0
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
            ataque= random.randint(False, True)
            moedas= random.randint(False, True)
            
            if escolha!= "ovo" and escolha!="papel" and escolha!= "bola" and escolha!= "livro":
                cenarios, nome_cenario_atual = carregar_cenarios()
                
                monstro=(cenario_atual["monstro"])
                hit=(cenario_atual["hit"])
                coins= (cenario_atual["coins"])
                if ataque==True and hit>0:
                    print("Um {0} te atacou, e tirou {1} da sua vida".format(monstro, hit))
                    life-= hit
                if moedas== True:
                    print("Você ganhou {0} coins nesta sala".format(coins))
                    moeda+= coins


            if (escolha == "ovo") or (escolha == "papel"):
                if escolha not in bolsa:
                    bolsa.append(escolha)
                    print ('voce coletou o item')
                if escolha in bolsa == True:
                     print('voce ja tem esse item')
            elif (escolha == "livro") or (escolha == "bola"):
                if escolha not in bolsa:
                    bolsa.append(escolha)
                    print ('voce coletou o item')
<<<<<<< HEAD
                    
            elif (escolha == "teleporte"):
                telep = input('para qual sala: ')
                if (telep == "biblioteca"):
                    nome_cenario_atual = "biblioteca"


                    
            elif (escolha == "professor"):
                if len(bolsa) <4:
                    print ('"nao falo com voce ate que pegue todos os itens."')
                    print ('"retorne ao lobby e nao volte ate conseguir"')
                    print ('-disse o professor')
                if len(bolsa) == 4:
                    print('huh, voce quer atrasar a entrega do EP?')
                    print('pois bem, quantos dias voce quer atrasar?')
                    print('seja razoavel, e lhe ajudarei')
                    print('seja ganancioso, e comerei a sua alma')
                    x = int(input('dias: '))
                    if (0 < x < 7):
                        print('Certo, achei justo')
                        print('------------------')
                        print('VOCE VENCEU O JOGO')
                        break
                    else:
                        print('CHEGA DE GRACINHAS, DEVORAREI SUA ALMA')
                        game_over = True
                        
                        
                    

=======
            elif (escolha == "teleporte"):
                x= input('para qual sala?: ')
                if (x == "biblioteca"):
                    nome_cenario_atual = "biblioteca"
>>>>>>> 8540eb165a1ec1853de1a26222393714a8924461


            elif escolha in opcoes:
                nome_cenario_atual = escolha

                
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True


    print("game over!") 

    if life<1:
        print("Você não resistiu ao ultimo monstro!")
    print("game over!")
    print("Você tinha {0} coins".format(coins))



# Programa principal.
if __name__ == "__main__":
    main()


    
    
    
    
    
    
    
    