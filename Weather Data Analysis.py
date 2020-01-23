# -*- coding: UTF-8 -*-
"""
Weather Data Analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Part 1 - by nested list
Part 2 - by pandas dataframe

1. Minimum temperature analysis
a) Average of minimum temperature for each month for the total period 
b) Average of minimum temperature for each month for each decade

2. Sun hours analysis
a) Average of sun hours for each month for the total period 
b) Average of sun hours for each month for each decade

:author: Gizem Tanriver

"""

####################
# PART 1 NESTED LIST
####################
# Importing modules for data visualization
from tabulate import tabulate

# Opening the file and reading as a nested list
with open("weather_data_Oxford_2019.txt", mode='r', encoding = 'utf-8') as f:
    for _ in range(7):
        next(f)
    data = []
    for line in f:
        list_of_words = line.split()  # Split the line on runs of whitespace
        data.append(list_of_words)

# Data Cleaning
for item in data:
    i = 0
    for string in item:
        # removing the string "Provisional" to make rows consistent (same number of elements)
        if string == "Provisional": item.remove(string)
        # removing "*" after a value
        for char in string:
            if char == "*": item[i] = string.translate({ord('*'): None}) # replacing "*" with None
        i += 1
# Convert string to numeric type
for item in data:
    for i in range(len(item)):
        if item[i]!='---': item[i] = float(item[i])

# 1. Analysis of Minimum Temperature
# a) Calculate average of minimum temperature for each month for the total data period
avg_tmin_monthly = {}
for month in range(1,13):
    sum_of_tmin = 0
    count_tmin = 0
    for item in data:
        if (item[1] == month) and (item[3] != '---'):
            sum_of_tmin += item[3]
            count_tmin += 1
    avg_tmin_monthly[month] = round(sum_of_tmin / count_tmin, 1)

print(tabulate( [list(avg_tmin_monthly.values())], headers=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep','Oct', 'Nov', 'Dec']))

# b) As per the table printed, July has the best weather with 12.3 C average temperature.

# c) Calculate average of minimum temperature for each month for each decade
# First decade incomplete 1853 to 1859
avg_tmin_decades = {}
avg_tmin_monthly = {}
for month in range(1,13):
    sum_of_tmin = 0
    count_tmin = 0
    for item in data[0: 7*12]:
        if (item[1] == month) and (item[3] != '---'):
            sum_of_tmin += item[3]
            count_tmin += 1
    avg_tmin_monthly[month] = round(sum_of_tmin / count_tmin, 1)
avg_tmin_decades['1853 - 1859'] = avg_tmin_monthly

# Decades from 1860 to 2019
for decade in range(1860, 2020, 10):
    avg_tmin_monthly = {}
    for month in range(1,13):
        sum_of_tmin = 0
        count_tmin = 0
        ind = min([index1 for index1,value1 in enumerate(data) if value1[0]==decade])
        for item in data[ind: ind+10*12]:
            if (item[1] == month) and (item[3] != '---'):
                sum_of_tmin += item[3]
                count_tmin += 1
        avg_tmin_monthly[month] = round(sum_of_tmin / count_tmin, 1)
    avg_tmin_decades['{} - {}'.format(decade, decade+9)] = avg_tmin_monthly

print ("{:<15} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format('Decade', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep','Oct', 'Nov', 'Dec'))
for decade, values in avg_tmin_decades.items():
    jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec = values.values()
    print ("{:<15} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format(decade, jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec))



# 2. Analysis of Sun Hours
# a) Calculate average sun hours for each month during the total data period
avg_sh_monthly = {}
for month in range(1,13):
    sum_of_sh = 0
    count_sh = 0
    for item in data:
        if (item[1] == month) and (item[6] != '---'):
            sum_of_sh += item[6]
            count_sh += 1
    avg_sh_monthly[month] = round(sum_of_sh / count_sh, 1)

print(tabulate( [list(avg_sh_monthly.values())], headers=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep','Oct', 'Nov', 'Dec']))

# b) As per the table printed, June has the best weather with 198.1 average sun hours.

# c) Calculate average of sun hours for each month for each decade
# First decade incomplete 1929
avg_sh_decades = {}
avg_sh_monthly = {}
for month in range(1,13):
    sum_of_sh = 0
    count_sh = 0
    # index where sunshine hours data starts
    ind = min([index1 for index1, value1 in enumerate(data) if value1[6] != '---'])
    for item in data[ind: ind+12]:
        if (item[1] == month) and (item[6] != '---'):
            sum_of_sh += item[6]
            count_sh += 1
    avg_sh_monthly[month] = round(sum_of_sh / count_sh, 1)
avg_sh_decades['1929 - 1929'] = avg_sh_monthly

# Decades from 1930 to 2019
for decade in range(1930, 2020, 10):
    avg_sh_monthly = {}
    for month in range(1,13):
        sum_of_sh = 0
        count_sh = 0
        ind = min([index1 for index1,value1 in enumerate(data) if value1[0]==decade])
        for item in data[ind: ind+10*12]:
            if (item[1] == month) and (item[6] != '---'):
                sum_of_sh += item[6]
                count_sh += 1
        avg_sh_monthly[month] = round(sum_of_sh / count_sh, 1)
    avg_sh_decades['{} - {}'.format(decade, decade+9)] = avg_sh_monthly

print ("{:<15} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format('Decade', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep','Oct', 'Nov', 'Dec'))
for decade, values in avg_sh_decades.items():
    jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec = values.values()
    print ("{:<15} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format(decade, jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec))




##################
# PART 2 - PANDAS
##################

# Importing modules
import pandas as pd
from tabulate import tabulate # used for visualization at the end

# Function to remove * after values to use when reading the file
def func(string):
    if "*" in string: return float(string.translate({ord('*'): None}))  # replacing "*" with None
    else: return float(string)

# Reading the file with pandas read_fwf function.
# Missing values are labeled as 'nan' by using the na_values parameter
dataset = pd.read_fwf("weather_data_Oxford_2019.txt", skiprows=[0,1,2,3,4,6], header=[0],
                      colspecs=[(0,8),(8,11),(11,20),(20,28),(28,36),(36,44),(44,50)], na_values='---',
                      converters={'tmin':func, 'sun':func}) # removing * after values

dataset['tmin'] = pd.to_numeric(dataset['tmin'])
dataset['sun'] = pd.to_numeric(dataset['sun'])


# 1. Analysis of Minimum Temperature
# a) Calculate average of minimum temperature for each month for the total data period

grouped_month = dataset.groupby("mm")
avg_tmin = (grouped_month['tmin'].mean()).round(1)
print('Average minimum temperature for each month for the total period', '\n')
print(tabulate( [list(avg_tmin.values)], headers=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep','Oct', 'Nov', 'Dec']))

# b) As per the table printed, July has the best weather with 12.3 C average temperature - same result as nested list.

# c) Calculate average of minimum temperature for each month for each decade

# First decade incomplete 1853 to 1859
avg_tmin_decades = {}
grouped_dec0 = dataset[0:84].groupby('mm')
avg_tmin_dec0 = (grouped_dec0['tmin'].mean()).round(1)
avg_tmin_decades['1853 - 1859'] = avg_tmin_dec0
# Decades from 1860 to 2019
decs = dataset[84:]
grouped_decs = decs.groupby([i//120 for i in range(len(decs))])
for dec in grouped_decs:
    grouped_dec = dec[1].groupby('mm')
    avg_tmin_dec = (grouped_dec['tmin'].mean()).round(1)
    avg_tmin_decades['{} - {}'.format(dec[1].iloc[0,0], dec[1].iloc[-1,0])] = avg_tmin_dec

print ("{:<15} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format('Decade', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep','Oct', 'Nov', 'Dec'))
for decade, values in avg_tmin_decades.items():
    jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec = values.values
    print ("{:<15} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format(decade, jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec))


# 2. Analysis of Sun Hours
# a) Calculate average sun hours for each month during the total data period

grouped_month = dataset.groupby("mm")
avg_sh = (grouped_month['sun'].mean()).round(1)
print('Average sun hours for each month for the total period', '\n')
print(tabulate( [list(avg_sh.values)], headers=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep','Oct', 'Nov', 'Dec']))


# b) As per the table printed, June has the best weather with 198.1 average sun hours - same result as nested list.

# c) Calculate average of minimum temperature for each month for each decade

# First decade incomplete 1853 to 1859
avg_sh_decades = {}
grouped_dec0 = dataset[912:924].groupby('mm')
avg_sh_dec0 = (grouped_dec0['sun'].mean()).round(1)
avg_sh_decades['1929 - 1929'] = avg_sh_dec0
# Decades from 1860 to 2019
decs = dataset[924:]
grouped_decs = decs.groupby([i//120 for i in range(len(decs))])
for dec in grouped_decs:
    grouped_dec = dec[1].groupby('mm')
    avg_sh_dec = (grouped_dec['sun'].mean()).round(1)
    avg_sh_decades['{} - {}'.format(dec[1].iloc[0,0], dec[1].iloc[-1,0])] = avg_sh_dec

print ("{:<15} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format('Decade', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep','Oct', 'Nov', 'Dec'))
for decade, values in avg_sh_decades.items():
    jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec = values.values
    print ("{:<15} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format(decade, jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec))

