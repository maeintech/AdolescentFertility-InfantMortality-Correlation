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
all_data = pd.read_excel('Life_exp.xls')

# Create United States DataFrame
US = all_data.loc[64016:64017, 'Indicator Name':]

# Add second batch of rows for United States
new_rows = all_data.loc[64079:64087, 'Indicator Name':]
US_data = US.append(new_rows)

# Final US DataFrame
print(US_data)


# Create DataFrame for Japan
Japan = all_data.loc[30356:30357, 'Indicator Name':]

# Add second batch of rows for Japan
new_rows = all_data.loc[30419:30427, 'Indicator Name':]
Japan_data = Japan.append(new_rows)

# Final Japan DataFrame
print(Japan_data)


# Create DataFrame for Syria
Syria = all_data.loc[57896:57897, 'Indicator Name':]

# Add second batch of rows for Syria
new_rows = all_data.loc[57959:57967, 'Indicator Name':]
Syria_data = Syria.append(new_rows)

# Final Syria DataFrame
print(Syria_data)


# Create DataFrame for Sudan
Sudan = all_data.loc[52541:52542, 'Indicator Name':]

# Add second batch of rows for Sudan
new_rows = all_data.loc[52604:52612, 'Indicator Name':]
Sudan_data = Sudan.append(new_rows)

# Final Sudan DataFrame
print(Sudan_data)
