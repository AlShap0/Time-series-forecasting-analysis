# Analysis of predictuve power of the SARIMA model 

## Project summary

In this project, the SARIMA model is used to produce forecasts for two very different time series- weather data, which is inherently very easy to predict, and the S&P 500 index, which is extremely difficult to predict. The purpose of the project is to examine the predictions produced by the SARIMA, and to try to understand what makes one TS so predictable, and what makes another TS so impossible to predict.

Data for the S&P 500 index is scraped using the yfinance API, and weather data is obtained from the Gov. of Canada records.

Data is cleaned either with the Python package Pandas (S&P), or with a bash script (weather data).

Predictions are then analyzed with various statistical methods and tests, and a Bayesian approach is also used to get deeper insight about the parameters of the SARIMA model.

## Which files to look at

The full report was written to report on the findings (see 'PHYS_321_Final_report.pdf').

Data cleaning, analysis, and visualizations are done in the jupyter notebook 'Time_Series_analysis_ARIMA_MCMC.ipynb'

The notebook 'weather_data_treatment.ipynb' holds all the data exploration and all the different things I tried while working on my project. It is very messy, but gives a good example of how I play around with data to get to know it and figure out the best results I can generate.

The 'src' folder contains the scripts used to clean the weather data, the 'data' folder contains all the cleaned weather data csv files, whereas the data/cleaned_data folder actually contains the raw weather data, and the 'images' folder contains all the figures and plots used for the final report.


Thank you!
