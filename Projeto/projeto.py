import json

def lerficheiro(fnome):
    f = open(fnome, encoding="UTF-8")
    bd = json.load(f)
    return bd


# Consultar um indivíduo na base de dados: a partir do CC/BI ou a partir do nome
def consulta(bd, procura):
    individuos = []
    for p in range(len(bd['pessoas'])):   
        listaValores = list(bd['pessoas'][p].values())
        nome, identi = listaValores[0], listaValores[4]
        nome2 = nome.split(" ")
        procura2 = procura.split(" ")
        n = 0
        while n < len(procura2):
            if procura2[n] in nome2:
                individuos.append(bd['pessoas'][p])
            n = n+1
        if procura == identi:
            individuos.append(bd['pessoas'][p])
    
    if individuos == []:
        individuos = "Não existe ninguém com o nome/CC/BI que atribuíste."
    return individuos



##### LISTAS #####


# Quantos indivíduos há na bd?
def numindiv(bd):
    i=0
    for p in bd['pessoas']:
        i=i+1
    return i


# Distribuição dos indivíduos por profissão
def distrib_prof(bd):
    distrib = {}
    for p in bd['pessoas']:
        if p['profissao'] in distrib.keys():
            distrib[p['profissao']] += 1
        else:
            distrib[p['profissao']] = 1
    return distrib


# Distribuição dos indivíduos por desporto - TOP10
def distrib_desporto(bd):
    distrib = {}
    for p in bd['pessoas']:
        for desporto in p['desportos']:
            if desporto in distrib.keys():
                distrib[desporto] += 1
            else:
                distrib[desporto] = 1
    return distrib

def ordenaValores(v):
    return v[1]

def top10(distrib):
    valores = list(distrib.items())
    valores.sort(key = ordenaValores)
    novaDistrib = dict(valores[-10:])
    return novaDistrib
