# A machine model that predicts the number of humans in the world
This project uses libraries such as: pandas, scikit-learn, numpy, matplotlib and seaborn.

The first step was to analyze the data. The data used comes from kaggle [Kaggle](https://www.kaggle.com/ahmethoso/wpp-population-by-age-and-sex) 
with a dataset of 66.893 rows and 71 columns containing data on the growth of populations of every country, continent and organization that exists. 

The data are categorized between the different age groups from 0 to 100 years and over and the sex of each population, from the years 1950 to 2100.

For the analysis of this dataset, the functions (Times Series) were used.

After loading the dataset and replacing the indexes with the Time columns.

![alt text](https://github.com/Dar-rius/PopulationAnalyze/blob/main/img/popSet.png)

The data of the LocID variable was displayed for the purpose of identifying the IDs of each country, continent and organization and the whole thing makes a total of 443 IDs, then the data of the Location variable to see all the countries, continents and organizations. contained in the dataset.

![alt text](https://github.com/Dar-rius/PopulationAnalyze/blob/main/img/ID.png)

![alt text](https://github.com/Dar-rius/PopulationAnalyze/blob/main/img/names.png)

After all this I moved on to the population analysis, the objective was to observe the growth of populations from 0 to 100 years and over in each country and continent according to their sex and then with the sexes combined between the 1950s to 2100.
To see graphs of other data I invite you to open the Analyze.ipynb file.

After having analyzed the male and female populations of each country, continent and organization. I analyzed the data of the populations of each continent according to their sex and then sum the 2 sexes in order to compare the growth of the population of each continent.
