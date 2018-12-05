'''
Goal: To create a package that will allow download of EIA STEO data sets. 
'''

import calendar
import datetime

# Creating a list of abbr months

month = []
for month_num in range(1, 13):
    mon = calendar.month_abbr[month_num].lower()
    month.append(mon)

# Finding the end point for the range of years

endyear = datetime.date.today().year - 1999

# Creating a 2 digit year list

year = list("%.2d" % x for x in range(8, endyear))

# Creating a key list of all the months and years

keys = []

for y in year:
    for m in month:
        keys.append(m+y)

#  Reviewing the EiA data showed that for the last months in 2013
#  the files were changed to xlsx format form xls
#  exceptions = ['aug13', 'sep13', 'oct13', 'nov13', 'dec13']

# Creating a dictionary of all the month year pairs and the appropriate file names.

dic = {}
for key in keys:
    if key == 'aug13' or key == 'sep13' or key == 'oct13' or key == 'nov13' or key == 'dec13':
        value1 = key + '_base.xlsx'
        value2 = key + '.pdf'
        dic.update({key: [value1, value2]})
    elif int(key[3:])<=13:
        value1 = key+'_base.xls'
        value2 = key+'.pdf'
        dic.update({key: [value1,value2]})
    else:
        value1 = key + '_base.xlsx'
        value2 = key + '.pdf'
        dic.update({key: [value1, value2]})


link = 'https://www.EIA.gov/outlooks/steo/archives/'

for key, value in dic.items():
    print(link+value[0])
    print(link+value[1])
