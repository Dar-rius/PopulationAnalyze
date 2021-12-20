#create functions to facilitate the analysis of different data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np


#fonction permettant de calculer le taux des pop dans diff regions
def calPopRegions(popO, popE, popS, popN, popC, popT, name):

    #Calcul de la population du taux des populations dans 
    #differentes regions,
    tauxO = (100*popO)/popT
    tauxE = (100*popE)/popT
    tauxS = (100*popS)/popT
    tauxN = (100*popN)/popT
    tauxC = (100*popC)/popT

    #Visualisation des donnees
    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

    recipe = ["population de l'ouest: %.2f" %tauxO,
            "population de l'est: %.2f" %tauxE,
            "population du sud: %.2f" %tauxS,
            "population du nord: %.2f" %tauxN,
            "population du centre: %.2f" %tauxC]

    data = [tauxO, tauxE, tauxS, tauxN, tauxC]

    wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40)

    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(arrowprops=dict(arrowstyle="-"),
            bbox=bbox_props, zorder=0, va="center")

    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1)/2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax.annotate(recipe[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                    horizontalalignment=horizontalalignment, **kw)

    ax.set_title(f"Croissance de la population dans les regions ({name})")

    plt.show()


#fonction permettant d'avoir le taux de la population totale dans chaque
#continent et de le comparrer entre eux
def continentTaux(popA, popB, popC, name ):
    #Le taux de la population totale 
    tauxM = (100*popA)/popC
    tauxF = (100*popB)/popC
    tauxT = [tauxM, tauxF]

    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

    recipe = ["Pop Male",
            "Pop Female",]

    #data = [float(x.split()[0]) for x in tauxT]
    population = [x.split()[-1] for x in recipe]


    def func(pct, allvals):
        absolute = int(np.round(pct/100.*np.sum(allvals)))
        return "{:.2f}%\n".format(pct, absolute)


    wedges, texts, autotexts = ax.pie(tauxT, autopct=lambda pct: func(pct, tauxT),
                                    textprops=dict(color="w"))

    ax.legend(wedges, population,
            title="population",
            loc="center left",
            bbox_to_anchor=(1, 0, 0.5, 1))

    plt.setp(autotexts, size=8, weight="bold")

    ax.set_title(f"La taux de la pop male et femelle en {name}")

    plt.show()



def continentTauxAll(popAfric, popAsia, popEurope, popOceanic, popNafta, popLatin , popTotale):

    #popAutre = (popAfric+popAsia+popEurope+popOceanic+popNafta+popLatin)-popTotale
    #tauxAutre = (100*popAutre)/popTotale
    tauxAfric = (100*popAfric)/popTotale
    tauxAsie = (100*popAsia)/popTotale
    tauxEu = (100*popEurope)/popTotale
    tauxOcean = (100*popOceanic)/popTotale
    tauxNaf = (100*popNafta)/popTotale
    tauxLatin = (100*popLatin)/popTotale

    data = { "Afrique: ": tauxAfric,
        "Asie " :tauxAsie,
        "Europe " :tauxEu,
        "Oceanique" :tauxOcean,
        "Nafta " :tauxNaf,
        "Amerique latine ":tauxLatin}

    print("La part de chaque continent dans la populaton totale:")
    for k, v in data.items():
        print(f"{k}: {v}")