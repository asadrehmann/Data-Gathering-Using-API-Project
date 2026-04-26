# Data engineering module 1-project

Description 
Introduction

This project focuses on applying Exploratory Data Analysis (EDA) to understand a real-world dataset obtained through an API. The goal is to explore the structure, quality, and patterns within the data before applying any machine learning techniques. EDA helps in identifying trends, detecting anomalies, and forming meaningful insights that guide further analysis and decision-making.

What We Did

In this assignment, we first obtained data using an API key and fetched the dataset programmatically. The data was then saved locally on our computer in a structured format (CSV/JSON). After loading the dataset into a data analysis environment, we performed EDA, including data cleaning, summary statistics, visualization, and interpretation of patterns. Finally, we derived insights from the data to understand its key characteristics.

Data Source

The dataset was collected using an API from TMDB. This API provides structured movie-related data such as popularity, ratings, vote counts, release dates, and other metadata. The data was retrieved in JSON format and converted into a tabular format suitable for analysis.

Processes Involved

The project followed a structured workflow:

Data Collection: Fetching data using an API key
Data Storage: Saving the raw data locally in JSON/CSV format
Data Loading: Importing the dataset into a Python environment using pandas
Data Cleaning: Handling missing values, checking duplicates, and correcting data types
Exploratory Data Analysis: Generating summary statistics, analyzing distributions, and visualizing relationships using plots
Insight Generation: Interpreting results to identify trends, patterns, and anomalies
Additional Information

During the analysis, it was observed that the dataset was relatively clean with minimal missing values and no duplicate records. Key variables such as popularity and vote count showed high variability, indicating that only a few movies dominate audience attention. Visualization techniques such as histograms and heatmaps were used to better understand distributions and relationships between variables. These findings provide a strong foundation for further predictive modeling.

References
TMDB API Documentation
Python (pandas, matplotlib, seaborn libraries)
Google Colab for data analysis environment