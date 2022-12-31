import json
import matplotlib.pyplot as plt

#Carregar a BD 
def carregarficheiro(fnome):
    bd = []
    f = open(fnome, encoding="UTF-8")
    bd=json.load(f)
    return bd

# Inserir um novo indivíduo na base de dados
def inserir(nome, idade, sexo, cidade, distrito, BI, descrição, profissao, party_abbr, party_name, religiao, desportos, 
            animais, figura_publica_pt, marca_carro, destinos_favoritos, fumador, gosta_cinema, gosta_viajar, acorda_cedo,
            gosta_ler, gosta_musica, gosta_comer, gosta_animais_estimacao, gosta_dancar, comida_favorita):

    insere = []
    pessoa={}
    pessoa['nome']=nome
    pessoa['idade']=idade
    pessoa['sexo']=sexo

    morada = {}
    morada['cidade'] = cidade
    morada['distrito'] = distrito
    pessoa['morada'] = morada

    pessoa['BI']=BI
    pessoa['descrição']=descrição
    pessoa['profissao']=profissao

    partido_politico = {}
    partido_politico['party_abbr'] = party_abbr
    partido_politico['party_name'] = party_name
    pessoa['partido_politico']=partido_politico 

    pessoa['religiao']=religiao
    pessoa['desportos']=[desportos]
    pessoa['animais']=[animais] 
    pessoa['figura_publica_pt']=figura_publica_pt
    pessoa['marca_carro']=marca_carro
    pessoa['destinos_favoritos']=[destinos_favoritos]

    atributos = {}
    atributos['fumador'] = fumador
    atributos['gosta_cinema'] = gosta_cinema
    atributos['gosta_viajar'] = gosta_viajar
    atributos['acorda_cedo'] = acorda_cedo
    atributos['gosta_ler'] = gosta_ler
    atributos['gosta_musica'] = gosta_musica
    atributos['gosta_comer'] = gosta_comer
    atributos['gosta_animais_estimacao'] = gosta_animais_estimacao
    atributos['gosta_dancar'] = gosta_dancar
    atributos['comida_favortita'] = comida_favorita
    pessoa['atributos'] = atributos
    
    pessoa['atributos']=atributos
    insere.append(pessoa)
    return insere


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

# Gráfico de distribuições
def plotdistrib(distrib, tipo): #tipo -> str
    fig=plt.figure(figsize=(20,7))
    plt.xlabel(tipo)
    plt.ylabel("Número de indivíduos")
    plt.bar(distrib.keys(), distrib.values(), color='green', width=0.3)
    plt.xticks([x for x in range(0, len(distrib.keys()))], distrib.keys())
    plt.title("Distribuição por " + tipo)
    plt.show()
    return
