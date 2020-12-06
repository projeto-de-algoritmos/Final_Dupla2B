
def gerar_caminhos(grafo, caminho, final):
    if caminho[-1] == final:
        yield caminho
        return

    for vizinho in grafo_valparaiso_ceilandia[caminho[-1]]:
        if vizinho in caminho:
            continue
        for caminho_maior in gerar_caminhos(grafo, caminho + [vizinho], final):
            yield caminho_maior


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
caminhos =[]
for caminho in gerar_caminhos(grafo_valparaiso_ceilandia, ['Valparaiso'], 'Ceilandia'):
    peso =0
    #print(caminho)
    c = caminho
    for i in range(len(caminho)-1):
        peso += grafo_valparaiso_ceilandia[caminho[i]][caminho[i+1]]
    caminhos.append([caminho, peso])
print(caminhos)