'''Data Visualization Project:
Part II: Take parsed data and visualize it using popular python math libraries'''

from collections import Counter

import csv
import matplotlib.pyplot as plt
import numpy as np

MY_FILE = '../data/sample_sfpd_incident_all.csv'

def parse(raw_file, delimiter):

	opened_file = open(raw_file)

	csv_data = csv.reader(raw_file, delimiter = delimiter)

	parsed_data = []

	fields = csv_data.next()

	for row in csv_data:
		parsed_data.appened(dict(zip(fields, row)))
	
	opened_file.close()

	return parsed_data

def visualize_days():
	'''Visualize data by day of week'''

	# grab our previously parsed data
	data_file = parse(MY_FILE, ",")

	# make a new variable, 'counter', from iterating through each line of
	# data in the parsed data, and count how many incidents happen on each
	# day of the week
	counter = Counter(item["DayOfWeek"] for item in data_file)

	# separate the x-axis data (the days of the week) from the 'counter'
	# variable from the y-axis data (the number of incidents for each day

	# with that y-axis data, assign it to a matplotlib plot instance

	# create the amount of ticks needed for our x-axis, and assign 
	# the labels

	# save the plot

	# close plot file



