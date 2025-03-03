Title: what machine learning can tell us about the future of the housing market across Canada

Aim: Using a dataset that shows the historical values of the housing price index in many different parts of Canada, an analysis on the trends will take place. 
Using data from 2018-2024, we are able to make some preliminary assessments of the situation by creating visualizations using tableau. This allows us to get an intial idea of these trends before jumping into predictions. 
Finally, this data will be fed into a long short-term memory machine learning algorithm (a type of neural network) to predict hoz these price index values will continue to change until 2030. The dataset was obtained from the following source - https://www.kaggle.com/datasets/noeyislearning/housing-price-indexes

All of the code was written by the three group members with occasional help from the Xpert AI tool.

PART 1 - DATA CLEANING - can be found within the file "cleaning.ipynb" which is in the "code" folder in the HousingPredictionsProject4 repository.
1) Dataset was loaded using Path and pd.read_csv.
2) The unnecessary columns were dropped by using the method of keeping the desired columns and attaching only those columns to the data.
3) The columns kept were renamed so as to be easier to understand using the .rename(columns={"...": "...."}).
4) Some filters were put in place to focus up our analysis - firstly, the dataset was filtered to begin in 2018. Secondly, the dataset was filtered so that the housing index value per location was only kept for the "total" housing type. In other words, we scrapped the division of "house only" or "land only" per location.
5) The cleaned dataset was saved as a new csv file to be used.


PART 2 - VISUALIZATIONS
Part 2.1 - tableau
An initial graph was generated using tableau to allow for some preliminary assessment of the data. The different locations were plotted seperately on the graph with the use of the dropdown menu allowing us to change location and thus get the correctly associated graph. The "date" variable was put into columns and the "index value" one into rows to generate the graph.

Based on this initial analysis, the housing markets with values that change significantly enough to carry out further analysis consists of the following major cities - Halifax (Nova Scotia), Montreal (Quebec), Ottawa-Gatineau (Ontario/Quebec), London (Ontario), Hamilton (Ontario), Toronto (Ontario), Calgary (Alberta), Vancouver (British Columbia), Victoria (British Columbia), Saskatoon (Saskatchewan), Winnipeg (Manitoba), Edmonton (Alberta) and Victoria (British Columbia).

Part 2.2 - long short-term memory used as a neural network to predict future index values for these cities until 2030

