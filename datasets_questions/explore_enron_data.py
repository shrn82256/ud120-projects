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

import cPickle as pickle
from pprint import pprint
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

hasTotPayments = 0
for key, value in enron_data.iteritems():
	if value["total_payments"] == "NaN" and value["poi"] == 1:
		hasTotPayments += 1

print hasTotPayments, len(enron_data)
# print([value["poi"] ].count(1))
# pprint(enron_data["SKILLING JEFFREY K"])