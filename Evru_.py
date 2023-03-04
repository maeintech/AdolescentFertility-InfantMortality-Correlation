#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 20:43:16 2023

@author: Mae
"""


# import modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# import data from csv file
def read(x):
    """
    Reads and imports files from excel spreadsheet to python

    Arguments:
    x: string, The name of the excel file which is to be read
    skiprows: integer, indicates the number of rows on the excel file to be
    skipped

    Returns:
    A pandas dataframe with all values from the excel file
    """
    W = pd.read_excel(x, skiprows=3)
    return W


# Read the data from World Bank excel file using the defined function
all_data = read('API_8_DS2_en_excel_v2_4777534.xls')

# Create separate pandas DataFrames for each country

# Create a DataFrame containing Indicators of interest in United States
United_States = all_data.loc[64012:64073, 'Indicator Name':]

# Add second batch of rows for United States DataFrame
new_rows = all_data.loc[64085:64094, 'Indicator Name':]
US_data = United_States.append(new_rows)

# transpose the Data Frame so index column is populated with years
US_data = US_data.transpose()

# convert the row containing indicators to a list
header = US_data.iloc[0].values.tolist()
US_data.columns = header  # make indicators the header for the DataFrame

US_data = US_data.iloc[2:]  # final US DataFrame

# Repeat the same steps to create the DataFrame for Japan
Japan = all_data.loc[30352:30413, 'Indicator Name':]

new_rows = all_data.loc[30425:30434, 'Indicator Name':]
Japan_data = Japan.append(new_rows)

Japan_data = Japan_data.transpose()
header = Japan_data.iloc[0].values.tolist()
Japan_data.columns = header

Japan_data = Japan_data.iloc[2:]  # final Japan DataFrame

# Repeat the same steps to create the DataFrame for Syrian Arab Republic
Syria = all_data.loc[57892:57953, 'Indicator Name':]

new_rows = all_data.loc[57965:57974, 'Indicator Name':]
Syria_data = Syria.append(new_rows)

Syria_data = Syria_data.transpose()
header = Syria_data.iloc[0].values.tolist()
Syria_data.columns = header

Syria_data = Syria_data.iloc[2:]  # final Syria DataFrame

# Repeat the same steps to create the DataFrame for Sudan
Sudan = all_data.loc[52537:52598, 'Indicator Name':]

new_rows = all_data.loc[52610:52619, 'Indicator Name':]
Sudan_data = Sudan.append(new_rows)

Sudan_data = Sudan_data.transpose()
header = Sudan_data.iloc[0].values.tolist()
Sudan_data.columns = header

Sudan_data = Sudan_data.iloc[2:]  # final Sudan DataFrame


# Now we want to visualise the infant mortality rate for the 4 countires
# over 60 years
# Slice the country DataFrames to identify total mortality rate of infants
# in each country from 1960 till 2021
def data(x, y):
    """"
    Slices a specific column on a DataFrame for  countries

    Arguments:
    x: pandas DataFrame, Name of DataFrame where the information is to be
    extracted from
    y: string, header name of the column to be sliced

    Returns:
    Column showing total mortality rate of infants from 1960 till 2021
    """
    r = x.loc['1960':'2021', y]
    return r


# Use defined function to get array containing Mortality rate of infants
# (from 1960 - 2021) in each country
US_x = data(US_data, 'Mortality rate, infant (per 1,000 live births)')
Japan_x = data(Japan_data, 'Mortality rate, infant (per 1,000 live births)')
Sudan_x = data(Sudan_data, 'Mortality rate, infant (per 1,000 live births)')
Syria_x = data(Syria_data, 'Mortality rate, infant (per 1,000 live births)')


# Create line graph for mortality rate of infants in each country over time
def line_graph(x, country_data, label):
    """
   Creates a line graph of specified variables

    Arguments:
    x: 1D array, contains values on the x-axis
    country_data: contains values for each point on the y-axis

    Returns:
    a line graph plotted based on inputted values on x and y axes
    """
    graph = plt.figure(figsize=(10, 6))

    plt.plot(x, country_data1, label=label1)  # line plot for country1
    plt.plot(x, country_data2, label=label2)  # line plot for country2
    plt.plot(x, country_data3, label=label3)  # line plot for country3
    plt.plot(x, country_data4, label=label4)  # line plot for country4

    plt.xlabel(x_label)  # label the x-axis
    plt.ylabel(y_label)  # label the y-axis
    plt.title(title, fontdict={'fontsize': 20}, pad=(10))  # title of the graph

    plt.xlim(min, max)  # specify the boundaries of the x-axis
    plt.legend()  # show a legend on the plot
    return graph


# Input values for the variables

x = US_data.index.astype(int)
# We can use the index of one country for the x-axis since these values are
# repeated for all countries

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
min = 1960
max = 2020


# Call the defined function to plot the desired graph
line_graph(x, country_data, label)

plt.savefig('Line Plot1')  # save the line plot
plt.show()  # display the line graph


# Investigate the correlation between infant mortality and teenage pregnancies

# Create a subplot function which plots two bar charts
def subplot(x, y1, y2):
    """
    Creates subplots containing two bar charts

    Arguments:
    x: 1D array, contains values for the x-axis on both bar charts
    y1: 1D array, contains values for the y-axis on the first bar chart
    y2: 1D array, contains values for the y-axis on the second bar chart

    Returns:
    a subplot figure containing two bar charts side by side for comparison
    """

    fig = plt.subplots(nrows=1, ncols=2, figsize=(11, 4))

    plt.subplot(1, 2, 1)  # create first subplot
    plt.bar(x, y1, color="black", alpha=0.5)  # first bar chart
    plt.xlabel(y1_xlabel)  # label the x-axis
    plt.ylabel(y1_ylabel, fontdict={'fontsize': 7})  # label the y-axis
    plt.title(y1_title, fontdict={'fontsize': 12}, pad=(10))  # title of chart1

    plt.subplot(1, 2, 2)  # create second subplot
    plt.bar(x, y2, color="green", alpha=0.8)  # second bar chart
    plt.xlabel(y2_xlabel)  # label the x-axis
    plt.ylabel(y2_ylabel, fontdict={'fontsize': 7})  # label the y-axis
    plt.title(y2_title, fontdict={'fontsize': 12}, pad=(10))  # title of chart2
    return fig


# Input values for variables
x = np.arange(2000, 2011, 1, dtype=int)  # values for x-axis

mortality = Syria_data.loc["2000":"2010",
                           'Mortality rate, infant (per 1,000 live births)']
y1 = mortality.values  # values for y-axis on first bar chart

fertility = Syria_data.loc[
            "2000":"2010",
            'Adolescent fertility rate (births per 1,000 women ages 15-19)']
y2 = fertility.values  # values for y-axis on second bar chart

y1_xlabel = 'Years'
y1_ylabel = "Mortality rate of infants (per 1,000 live births)"
y1_title = "Mortality rate of infants in Syria"

y2_xlabel = "Years"
y2_ylabel = 'Adolescent fertility rate (births per 1,000 women ages 15-19)'
y2_title = "Adolescent fertility rate in Syria"

# Call the defined function to plot the bar charts
subplot(x, y1, y2)

plt.savefig('Bar Charts2')  # save the charts
plt.show()  # display the lcharts


# Investigate whether adolescent fertility is reducing because the
# population of adolescents in the country is also reducing

# Create a function to extract population of women of Child bearing age for a
# particular year
def s(x, y, z):
    """
    Slices specific rows and columns from a given DataFrame

    Arguments:
    x: pandas DataFrame, the DataFrame to be sliced
    y: the row(s) to be sliced
    z: the column(s) to be sliced

    Returns:
    values from rows/columns on the DataFrame which has been sliced
    """

    f1 = x.loc[y, z]
    return f1


# Input values for the function to obtain figures for population of women of
# child bearing age in Syria (for year 2000 and 2010)
x = Syria_data
y1 = "2000"

a = s(x, y1, 'Population ages 15-19, female (% of female population)')
b = s(x, y1, 'Population ages 20-24, female (% of female population)')
c = s(x, y1, 'Population ages 25-29, female (% of female population)')
d = s(x, y1, 'Population ages 30-34, female (% of female population)')
e = s(x, y1, 'Population ages 35-39, female (% of female population)')
f = s(x, y1, 'Population ages 40-44, female (% of female population)')

x = Syria_data
y2 = "2010"

g = s(x, y2, 'Population ages 15-19, female (% of female population)')
h = s(x, y2, 'Population ages 20-24, female (% of female population)')
i = s(x, y2, 'Population ages 25-29, female (% of female population)')
j = s(x, y2, 'Population ages 30-34, female (% of female population)')
k = s(x, y2, 'Population ages 35-39, female (% of female population)')
l = s(x, y2, 'Population ages 40-44, female (% of female population)')

# Create arrays containing values for % of female population of
# child bearing age in 2000 and 2010
female_pop1 = np.array([a, b, c, d, e, f])  # for year 2000
female_pop2 = np.array([g, h, i, j, k, l])  # for year 2010


# Create a subplot function which plots two pie charts
def subplot_pie(p1, p2):
    """
    Creates subplots containing two pie charts

    Arguments:
    p1: 1D array, contains data to be plotted for the first pie chart
    p2: 1D array, contains data to be plotted for the second pie chart

    Returns:
    a subplot figure containing two pie charts side by side for comparison
    """

    fig = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))

    plt.subplot(1, 2, 1)
    plt.pie(p1, explode=explode, colors=color, autopct='%.1f%%',
            startangle=90, textprops=dict(fontsize=8))  # first pie chart
    plt.title(title1, fontdict={'fontsize': 8})  # title of chart1

    plt.subplot(1, 2, 2)
    plt.pie(p2, explode=explode, colors=color, autopct='%.1f%%',
            startangle=90, textprops=dict(fontsize=8))  # second pie chart
    plt.title(title2, fontdict={'fontsize': 8})  # # title of chart2

    plt.legend(labels=label, loc='lower right', title=title_legend,
               bbox_to_anchor=(1.5, -0.1))  # legend for both charts
    return fig


# Input values for each variable
p1 = female_pop1
p2 = female_pop2

# explode the first wedge corresponding to % of females aged 15-19
explode = [0.15, 0, 0, 0, 0, 0]

color = ['magenta', 'orange', 'green', 'grey', 'purple', 'pink']
title1 = "Percentage of Female population of Child-Bearing age (Syria, 2000)"
title2 = "Percentage of Female population of Child-Bearing age (Syria, 2010)"
label = ['15-19', '20-24', '25-29', '30-34', '35-39', '40-44']
title_legend = 'Age Ranges'

# Call the defined function to plot the desired graph
subplot_pie(p1, p2)

plt.savefig('Pie Charts3')   # save the charts
plt.show()  # display the charts
