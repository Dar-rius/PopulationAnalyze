#create functions to facilitate the analysis of different data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 


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
    print(dataTotal.head())
    print("Data sex total: ")
    print(dataT.head())
    sns.lineplot(data=dataTotal) 
    sns.lineplot(data=dataT)

# pour un seul pays 
def calNumberDecenies(dataA, dataB, dataC, dataD):
    print("Data male:")
    print("DataA:")
    print(dataA.head())
    print("DataB:")
    print(dataB.head())
    dataTotalMale = dataA+dataB
    dataTotalMaleFrame = pd.DataFrame(dataTotalMale)
    print('dataTotal')
    print(dataTotalMaleFrame.head())

    print("Data female:")
    print("DataC:")
    print(dataC.head())
    print("DataD:")
    print(dataD.head())
    dataTotalFemale = dataC+dataD
    dataTotalFemaleFrame = pd.DataFrame(dataTotalFemale)
    print('dataTotal')
    print(dataTotalFemaleFrame.head())
    #merge series and display a graph
    dataTotal = pd.merge(dataTotalMaleFrame, dataTotalFemaleFrame, on="Time", how='inner')
    sns.lineplot(data=dataTotal) 

# pour 10 pays 
def calNumberDeceniesTotal(dataA, dataB, dataC, dataD):
    
    dataTotalMale = dataA+dataB
    dataTotalFemale = dataC+dataD
    dataTotal = dataTotalMale + dataTotalFemale
    dataTotalFrame = pd.DataFrame(dataTotal)
    print(dataTotalFrame.head())
    #graph
    sns.lineplot(data=dataTotal) 