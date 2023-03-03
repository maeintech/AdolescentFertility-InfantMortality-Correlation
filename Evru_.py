#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 20:43:16 2023

@author: Mae
"""


# import packages
import pandas as pd
import matplotlib.pyplot as plt


# import data from csv file
def read(x):
    """
    Reads and imports files from excel spreadsheet to python

    Arguments:
    x: string, The name of the excel file which is to be read
    skiprows: integer, indicates the number of rows on the excel file to be
    skipped

    Returns:
    W: A pandas dataframe with all values from the excel file
    """
    W = pd.read_excel(x, skiprows=3)
    return W


# Read the data from World Bank using the defined function
all_data = read('API_8_DS2_en_excel_v2_4777534.xls')

# Create a separate pandas DataFrame for Indicators of interest in data for
# United States
United_States = all_data.loc[64012:64073, 'Indicator Name':]

# Add second batch of rows for United States DataFrame
new_rows = all_data.loc[64085:64094, 'Indicator Name':]
US_data = United_States.append(new_rows)

# Manipulating the DataFrame to give desired layout
US_data = US_data.transpose()
header = US_data.iloc[0].values.tolist()
US_data.columns = header
US_data = US_data.iloc[2:]

# Create a separate pandas DataFrame for Indicators of interest in data for
# Japan
Japan = all_data.loc[30352:30413, 'Indicator Name':]

# Add second batch of rows for Japan DataFrame
new_rows = all_data.loc[30425:30434, 'Indicator Name':]
Japan_data = Japan.append(new_rows)

# Manipulating the DataFrame to give desired layout
Japan_data = Japan_data.transpose()
header = Japan_data.iloc[0].values.tolist()
Japan_data.columns = header
Japan_data = Japan_data.iloc[2:]

# Create a separate pandas DataFrame for Indicators of interest in data for
# Syrian Arab Republic
Syria = all_data.loc[57892:57953, 'Indicator Name':]

# Add second batch of rows for Syria DataFrame
new_rows = all_data.loc[57965:57974, 'Indicator Name':]
Syria_data = Syria.append(new_rows)

# Manipulating the DataFrame to give desired layout
Syria_data = Syria_data.transpose()
header = Syria_data.iloc[0].values.tolist()
Syria_data.columns = header
Syria_data = Syria_data.iloc[2:]

# Create a separate pandas DataFrame for Indicators of interest in data for
# Sudan
Sudan = all_data.loc[52537:52598, 'Indicator Name':]

# Add second batch of rows for Sudan DataFrame
new_rows = all_data.loc[52610:52619, 'Indicator Name':]
Sudan_data = Sudan.append(new_rows)

# Manipulating the DataFrame to give desired layout
Sudan_data = Sudan_data.transpose()
header = Sudan_data.iloc[0].values.tolist()
Sudan_data.columns = header
Sudan_data = Sudan_data.iloc[2:]


# Slice the columns for total mortality rate of infants in each country from
# 1960 till 2021
def data(x):
    """"This function is used to slice the column for Mortality rates of
    infants per 1,000 live births from years 1960 to 2021]

    Arguments:
    x: string, Name of DataFrame where the information is to be extracted from

    Returns:
    Column showing total mortality rate of infants from 1960 till 2021"""
    r = x.loc['1960':'2021', 'Mortality rate, infant (per 1,000 live births)']
    return r


# Use defined function to get Mortality rate of infants in each country
US_x = data(US_data)
Japan_x = data(Japan_data)
Sudan_x = data(Sudan_data)
Syria_x = data(Syria_data)


# Create line graph for mortality rate of infants in each country over 60 years
def line_graph(x, country_data, label):
    """
    This function will create a line graph of specified variables

    Arguments:
    x: 1D array, contains values on the x-axis
    country_data: contains values for each point on the y-axis

    Returns:
    graph: a line graph plotted based on inputted values
    """

    graph = plt.figure(figsize=(10, 6))

    plt.plot(x, country_data1, label=label1)  # line plot for country1
    plt.plot(x, country_data2, label=label2)  # line plot for country2
    plt.plot(x, country_data3, label=label3)  # line plot for country3
    plt.plot(x, country_data4, label=label4)  # line plot for country4
    plt.xlabel(x_label)  # label the x-axis
    plt.ylabel(y_label)  # label the y-axis
    plt.title(title)  # title of the graph

    plt.legend()  # show a legend on the plot
    return graph


# Input values for variables
x = US_data.index.astype(int)  # We can use the index of one country for the
# x-axis since these values are repeated for all countries

# Input variables for mortality rate in each country as previously defined
country_data1 = US_x
country_data2 = Japan_x
country_data3 = Syria_x
country_data4 = Sudan_x

# Create an array for all country data to be plotted on the graph
country_data = [country_data1, country_data2, country_data3, country_data4]

# Input values for labels on each line on the graph
label1 = 'United States'
label2 = 'Japan'
label3 = 'Syrian Arab Republic'
label4 = 'Sudan'

# Create an array for all labels to be plotted on the graph
label = [label1, label2, label3, label4]

# Input all other variables
x_label = 'Years'
y_label = 'Mortality rate of infants (per 1,000 live births)'
title = 'Mortality rate of infants in Japan, US, Syria and Sudan'


# Call the defined function to plot the desired graph
line_graph(x, country_data, label)

plt.show()  
