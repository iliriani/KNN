import numpy as np
import sqlalchemy as sqlal
import filterindataPearson as f
import recommender as r


users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0,
                      "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bill": {"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5,
                  "Vampire Weekend": 3.0},
         "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5,
                  "Slightly Stoopid": 1.0},
         "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5,
                 "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0,
                    "Vampire Weekend": 1.0},
         "Jordyn": {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5,
                    "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0,
                 "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5,
                      "The Strokes": 3.0}
         }




persoruesit={"Agoni":{"avatari":3.5,"titaniku":2,"Puirsiut":0,"remeber me":4.5,"Weird":5,"shok":1.5,"mentalist":2.5,"galileo":2},
             "Teuta":{"avatari":3,"titaniku":0,"Puirsiut":0,"remeber me":5,"Weird":4,"shok":2.5,"mentalist":3,"galileo":0}}


# print(f.kos_distanca(persoruesit["Agoni"],persoruesit["Teuta"]))
emri='Veronica'

person=f.pearson(users[''+emri+''],users['Jordyn'])



def Knn_rekomandimi(k,emri):

    afersite_emrit={}
    # I gjejme sipas algoritmit vlerat e gjithe perdoruesve
    for emrat in users:
        if emrat != emri:
            nje_item = f.pearson(users[''+emri+''], users[''+emrat+''])
            afersite_emrit [str(nje_item)] = str(emrat)

    # Renditet Lista nga me te afertit
    afersite_emrit_renditur = {}
    for key in sorted(afersite_emrit, reverse=True):
        afersite_emrit_renditur[str(key)] = afersite_emrit[key]

    # I marrim vetem k perdoresit me te afert
    lista_ngushte = {}
    x = 0
    for element in afersite_emrit_renditur:
        if x < k:
            lista_ngushte[str(element)] = afersite_emrit_renditur[element]
            x+=1

    # llogarisim hisen e secilit person ne ngjashmerine e emrit
    shuma = 0.0
    for numrat in lista_ngushte:
        shuma += (float)(numrat)

    hisja = []
    for numrat in lista_ngushte:
        useri = lista_ngushte[numrat]
        userat = [ useri, (float)(numrat)/shuma]
        hisja.append(userat)

    # I gjejme gjitha entitetet sipas fqinjeve te emrit
    gjitha_entitetet = {}
    i = 0
    for entet in hisja:
        te_userit = users[hisja[i][0]]
        gjitha_entitetet[str(hisja[i][0])] = te_userit
        i += 1

    # I vendosim gjitha entitetet ne nje matric
    krejt_tabela=[]
    i=0
    entitet_shokeve = []
    for key1,value1 in gjitha_entitetet.items():
        for key2, value2 in value1.items():
                emri_shokut = hisja[i][0]
                hisja_emrit = hisja[i][1]
                enti = key2
                if enti not in entitet_shokeve:
                    entitet_shokeve.append(enti)
                vlera = value2
                prod = hisja_emrit*vlera
                bashke = [emri_shokut,enti,vlera,prod]
                krejt_tabela.append(bashke)

    # Njehsojme mases e secilit entitet
    rekomandimmet ={}
    for enti in entitet_shokeve:
        shuma = 0.0
        for rreshti in krejt_tabela:
            if rreshti[1] == enti:
                shuma += rreshti[3]
                rekomandimmet[str(enti)] = shuma

    # Sotojme rekomandimet nga ato me masen me te madhe deri te ato me te voglat
    rekomando = {}
    sorto = sorted(rekomandimmet, key=lambda x: rekomandimmet[x], reverse=True)
    for ki in sorto:
        if ki not in users[str(emri)]:
            rekomando[str(ki)] = rekomandimmet[ki]

    print('Rekomandimet per ',emri)
    return rekomando

print(Knn_rekomandimi(2,'Veronica'))
