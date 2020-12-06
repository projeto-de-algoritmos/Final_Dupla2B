import dijkstra
import engarrafamento
import rota
grafo_valparaiso_ceilandia = { 
        "Valparaiso" : { "SantaMaria" : 3.5 },
        "SantaMaria" : {"EPTC": 9.5, "GuaraII":22.5, "CruzeiroNovo": 32.4},
        "GuaraII" : { "CruzeiroNovo": 9.9, "SamambaiaSul": 14.2 },
        "EPTC" : { "GuaraII": 13, "CruzeiroNovo": 23.9, "SamambaiaSul":16.9},
        "CruzeiroNovo" : { "Ceilandia": 26.4 },
        "SamambaiaSul": {"Ceilandia": 13.1 , "BR-070": 24.3},
        "BR-070": {"Ceilandia": 9.6},
        "Ceilandia": { }
        }

grafo = {}
melhorrota = ""

def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. insere engarramento em algum caminho")
    print("2. Mostra o melhor caminho do valparaiso a ceilandia") 
    print("3. Abre o maps com o melhor caminho")
    print("4. Sair")
    print(67 * "-")
  


if __name__ == '__main__':
    loop=True
    
    while loop:
        print_menu()
        choice = input("Entre sua opcao [1-4]: ")            
        if choice=='1':
            print("Opcao 2 foi escolhida")
            print("os pontos de referencias de valparaiso a ceilandia: SantaMaria, EPTC, GuaraII, CruzeiroNovo, SamambaiaSul , BR-070\n")
            inicio_engarrafamento = input('digite o inicio do engarrafamento\n')
            fim_engarrafamento = input('digite o fim do engarrafamento\n')
            c = input("Digite 1 para engarrafamento leve - 2 para engarrafamento moderado - 3 para engarrafamento pesado\n: ")
            if c=='1':
                    tipoengarrafamento = "leve"
            if c=='2':
                    tipoengarrafamento = "moderado"
            if c=='3':
                    tipoengarrafamento = "pesado"
            grafo = engarrafamento.main(grafo_valparaiso_ceilandia,inicio_engarrafamento,fim_engarrafamento, tipoengarrafamento)    
        elif choice=='2':
            print("Opcao 3 foi escolhida")
            if grafo != {}:
                melhorrota = dijkstra.dijkstra_distancia(grafo,"Valparaiso","Ceilandia")
            else:
                melhorrota = dijkstra.dijkstra_distancia(grafo_valparaiso_ceilandia,"Valparaiso","Ceilandia")           
        elif choice=='3':
            print("Opcao 4 foi escolhida")
            if melhorrota == "":
                print("Escolha uma rota usando opção 3")
            else:   
                rota.main(melhorrota)
        elif choice=='4':
            print("Opcao 5 foi escolhida")
            print('Saindo....')
            loop=False
        else:
            input("Opcao incorreta. Aperte qualquer tecla para tentar novamente..")
