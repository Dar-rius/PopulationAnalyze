#create functions to facilitate the analysis of different data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np

#A function allowing to convert two variables which contains 
# the number of men and women according to a base age in float 
# in int, to display the 5 1st elements of the column to then merge 
# the columns and create a new dataframe for at the end make a graph

# pour un seul pays
def calPopMaleFemale(dataM, dataF, dataCountry, dataT):
    print(dataCountry)
    print("Graph de la population masculine et femine et mondiale:")
    #merge series and display a graph
    print("Data male and female: ")
    dataTotal = pd.merge(dataM, dataF, on="Time", how='inner')
    print(dataTotal)
    print("Data sex total: ")
    print(dataT)
    sns.lineplot(data=dataTotal) 
    sns.lineplot(data=dataT)
