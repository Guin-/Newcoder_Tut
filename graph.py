'''Data Visualization Project:
Part II: Take parsed data and visualize it using popular python math libraries'''

from collections import Counter

import csv
import matplotlib.pyplot as plt
import numpy as np
from parse import parse

MY_FILE = "../data/sample_sfpd_incident_all.csv"


def visualize_days():
	'''Visualize data by day of week'''

	# grab our previously parsed data
	data_file = parse(MY_FILE, ",")

	# make a new variable, 'counter', from iterating through each line of
	# data in the parsed data, and count how many incidents happen on each
	# day of the week
#	for item in data_file:
#		counter = Counter(item['DayOfWeek'])
	counter = Counter(item["DayOfWeek"] for item in data_file)
	# use list data struct to manually set each counter key to preserve order	
	data_list = [ 
			counter["Monday"],
			counter["Tuesday"],
			counter["Wednesday"],
			counter["Thursday"],
			counter["Friday"],
			counter["Saturday"],
			counter["Sunday"]
			]

	day_tuple = tuple(['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'])

	# separate the x-axis data (the days of the week) from the 'counter'
	# variable from the y-axis data (the number of incidents for each day

	# with that y-axis data, assign it to a matplotlib plot instance
	plt.plot(data_list)

	plt.xticks(range(len(day_tuple)), day_tuple)

	# save the plot
	plt.savefig("Days.png")

	# close plot file
	plt.clf()

def visualize_type():
	'''Visualize data by category in a bar graph'''

	# Get parsed data file	
	data_file = parse(MY_FILE, ",")

	# Create a tally for each item under Category in the file	
	counter = Counter(item["Category"] for item in data_file)

	# Create a tuple of the different keys to place on x-axis
	labels = tuple(counter.keys())

	# Set locations of the x ticks(labels)
	xlocations = np.arange(len(labels)) + 0.5
	
	# Set width of each bar
	width = 0.5

	# Assign the data to a bar plot (values = tally)
	plt.bar(xlocations, counter.values(), width = width)

	# Set the x ticks to be in the middle of each bar, with keys from the label tuple, and a 90 degree rotation	
	plt.xticks(xlocations + width / 2, labels, rotation = 90)

	# Give more space for the labels
	plt.subplots_adjust(bottom = 0.4)

	# Change/increase the size of the window that contains the graph
	plt.rcParams['figure.figsize'] = 12, 8

	# Save the graph
	plt.savefig("Type.png")

	# Close the file
	plt.clf()






def main():
#	visualize_days()
	visualize_type()
if __name__ == "__main__":
	main()



