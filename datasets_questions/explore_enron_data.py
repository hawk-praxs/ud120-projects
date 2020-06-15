#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle
import pandas as pd
import math

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl"
                              , "rb"))

print('Size of Enron Data: ', len(enron_data))

print('No.of features: ', len(enron_data['SKILLING JEFFREY K']))

count = 0

for key in list(enron_data.keys()):
    if enron_data[key]['poi'] == 1:
        count+=1

print('POIs in the dataset: ', count)

with open("../final_project/poi_names.txt") as f:
    names = f.readlines()

names = [x.strip() for x in names]
print('No. of total POIs: ', len(names)-2)

print('Total value of the stock belonging to James Prentice: ',
      enron_data['PRENTICE JAMES']['total_stock_value'])

print('No. of emails from Wesley Colwell to POI: ',
      enron_data['COLWELL WESLEY']['from_this_person_to_poi'])

print('Value of stock options exercised by Jeffrey K Skilling: ',
      enron_data['SKILLING JEFFREY K']['exercised_stock_options'])

print('Money obtained by Kenneth Lay: ',
      enron_data['LAY KENNETH L']['total_payments'])

print('Money obtained by Jeffrey K Sklling: ',
      enron_data['SKILLING JEFFREY K']['total_payments'])

print('Money obtained by Andrew Fastow: ',
      enron_data['FASTOW ANDREW S']['total_payments'])

count = 0
for key in enron_data:
    if not(math.isnan(float(enron_data[key]['salary']))):
        count+=1

print('People with quantified salary: ', count)

count = 0
for key in enron_data:
    if enron_data[key]['email_address'] != 'NaN':
        count+=1

print('People with quantified salary: ', count)

count = 0
for key in enron_data:
    if math.isnan(float(enron_data[key]['total_payments'])):
        count+=1

print('% of people having NaN for total payments: ', count/len(enron_data)*100)

count = 0
for key in enron_data:
    if math.isnan(float(enron_data[key]['total_payments'])):
        count+=1

print('People with NaN for total payments: ', count)

count = 0
for key in enron_data:
    if enron_data[key]['poi']==1 and math.isnan(float(enron_data[key]['total_payments'])):
        count+=1

print('% of POIs having NaN for total payments: ', count/35)