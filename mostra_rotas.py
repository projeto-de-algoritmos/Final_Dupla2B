
def gerar_caminhos(grafo, caminho, final):
    if caminho[-1] == final:
        yield caminho
        return

    for vizinho in grafo[caminho[-1]]:
        if vizinho in caminho:
            continue
        for caminho_maior in gerar_caminhos(grafo, caminho + [vizinho], final):
            yield caminho_maior


def merge_sort(vet):
    if len(vet)>1:
        mid = len(vet)//2
        lefthalf = vet[:mid]
        righthalf = vet[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i][1] < righthalf[j][1] :
                vet[k]=lefthalf[i]
                i=i+1
            else:
                vet[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            vet[k] =lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            vet[k]=righthalf[j]
            j=j+1
            k=k+1

def main(grafo_valparaiso_ceilandia):
    caminhos =[]
    for caminho in gerar_caminhos(grafo_valparaiso_ceilandia, ['Valparaiso'], 'Ceilandia'):
        peso =0
        c = caminho
        for i in range(len(caminho)-1):
            peso += grafo_valparaiso_ceilandia[caminho[i]][caminho[i+1]]
        caminhos.append([caminho, peso])
    merge_sort(caminhos)
    return caminhos

