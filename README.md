# Housing Index Price Analysis

## Project Overview

This project aims to explore the future trends of the Canadian housing market using historical housing price index data. By analyzing data from 2018-2024, we first create visualizations to better understand the initial patterns and trends. These trends are then fed into a Long Short-Term Memory (LSTM) neural network model, a type of machine learning algorithm, to predict how housing price indices will change until 2030. The dataset used for this analysis is sourced from [Kaggle: Housing Price Indexes](https://www.kaggle.com/datasets/noeyislearning/housing-price-indexes).

All of the code for this project was written by the group members, with occasional assistance from the Xpert AI tool.

## Table of Contents
- [Project Overview](#project-overview)
- [Objectives](#objectives)
- [Technologies Used](#technologies-used)
- [Data Sources](#data-sources)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Part 1 - Data Cleaning](#part-1---data-cleaning)
- [Part 2 - Visualizations](#part-2---visualizations)
  - [Part 2.1 - Tableau](#part-21---tableau)
  - [Part 2.2 - LSTM Predictions](#part-22---lstm-predictions)

- [License](#license)

## Objectives
The primary objective of this project is to analyze the historical trends in housing prices across Canada and predict future values until 2030. The specific tasks include:
- **Data Cleaning**: Preprocess the dataset to ensure it is in a suitable format for analysis and model building.
- **Data Visualization**: Create initial visualizations to identify key trends and locations of interest.
- **Prediction**: Use machine learning (LSTM) to forecast future housing price trends.

## Technologies Used
- **Python**: Main programming language used for data analysis, cleaning, and machine learning.
- **Pandas**: Used for data manipulation and cleaning.
- **NumPy**: For numerical operations.
- **Matplotlib & Seaborn**: For plotting and visualizing data.
- **TensorFlow & Keras**: For building and training the Long Short-Term Memory (LSTM) model.
- **Tableau**: Used for creating interactive visualizations of the data.
- **Jupyter Notebook**: For running Python code interactively.

## Data Sources
- **Kaggle Dataset**: The housing price index data for various Canadian cities was obtained from Kaggle.
  
    [Kaggle Dataset Link](https://www.kaggle.com/datasets/noeyislearning/housing-price-indexes)

## Project Structure


## Setup and Installation

### Prerequisites
- Python 3.7 or higher
- Necessary Python libraries (listed in `requirements.txt`)

### Installation Steps:
1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/HousingPredictionsProject4.git
    cd HousingPredictionsProject4

## Usage

### Part 1 - Data Cleaning
The data cleaning process is handled in the `cleaning.ipynb` file. Here’s a summary of the steps:
- **Dataset Loading**: The dataset is loaded using the `Path` method and `pd.read_csv`.
- **Column Filtering**: Unnecessary columns are removed, and only relevant columns are retained for analysis.
- **Renaming Columns**: Columns are renamed for clarity and easier understanding.
- **Data Filtering**: The dataset is filtered to include only the "total" housing type per location and data starting from 2018.
- **Saving Cleaned Data**: The cleaned data is saved as a new CSV file (`cleaned_data.csv`) for further use.

### Part 2 - Visualizations
#### Part 2.1 - Tableau
An initial visualization is created using **Tableau** to provide a preliminary understanding of the trends in the data. This includes:
- Plotting the housing index values by location.
- Using a dropdown menu to switch between different locations.
- Displaying the `date` variable in columns and the `index value` in rows.

#### Part 2.2 - LSTM Predictions
To predict future housing price indices, an LSTM model is built and trained. Key steps include:
- **City Selection**: The cities of interest are filtered using `df["Geography"].unique()`.
- **Sequence Creation**: A function (`create_sequences`) is defined to manage the data sequences for prediction.
- **Model Training**: The LSTM model is trained on the filtered data.
- **Prediction**: After training, the model generates predictions for future housing price indices.
- **Visualization**: A plot is created to visualize the predicted trends until 2030.

A **dropdown menu** is added using `widgets.dropdown` to allow users to switch between different locations.

![Flowchart](C:\Users\Muskan\Desktop\HousingPredictionsProject4\Resources\Activity diagram - Page 2.png)



## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

