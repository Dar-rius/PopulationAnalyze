#create functions to facilitate the analysis of different data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 


#A function allowing to convert two variables which contains 
# the number of men and women according to a base age in float 
# in int, to display the 5 1st elements of the column to then merge 
# the columns and create a new dataframe for at the end make a graph


def calNumber(dataA, dataB):
    #merge series and display a graph
    dataTotal = pd.merge(dataA, dataB, on="Time", how='inner')
    print(dataTotal.head())
    sns.lineplot(data=dataTotal) 


def calNumberDecenies(dataA, dataB, dataC, dataD):
    
    dataTotalMale = dataA+dataB
    dataTotalMaleFrame = pd.DataFrame(dataTotalMale)
    print(dataTotalMaleFrame.head())

    dataTotalFemale = dataC+dataD
    dataTotalFemaleFrame = pd.DataFrame(dataTotalFemale)
    print(dataTotalFemaleFrame.head())
    #merge series and display a graph
    dataTotal = pd.merge(dataTotalMaleFrame, dataTotalFemaleFrame, on="Time", how='inner')
    sns.lineplot(data=dataTotal) 


def calNumberDeceniesTotal(dataA, dataB, dataC, dataD):
    
    dataTotalMale = dataA+dataB
    dataTotalFemale = dataC+dataD
    dataTotal = dataTotalMale + dataTotalFemale
    dataTotalFrame = pd.DataFrame(dataTotal)
    print(dataTotalFrame.head())
    #graph
    sns.lineplot(data=dataTotal) 