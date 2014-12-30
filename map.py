"""
Data Visualization Project

Part III: Use the previously parsed data to create a different format to render a map. 
Parse through each line of the CSV file and create a geojson object to be collected 
into one geojson file for uploading to a github gist. 
"""

import geojson

import parse as p

def create_map(data_file):
	'''
	Creates a GeoJSON file. 

	Returns a GeoJSON file that can be rendered in a gist. Copy the output file
	and paste into a new Gist. Github will render the GeoJSON file as a map.
	'''

	# Define the type of GeoJSON file being created
	geo_map = {"type": "FeatureCollection"}

	# Create an empty list to collect points to graph
	item_list = []

	# Iterate over data to create a GeoJSON document
	# Use enumerate to get both the line and line number
	for index, line in enumerate(data_file):
		
		# Skip any zero coordinates
		if line['X'] == "0" or line['Y'] == "0":
			continue

		# Create a new dictionary for each iteration
		data = {}

		# Assign line items to appropraite GeoJSON fields
		data['type'] = 'Feature'
		data['id'] = index
		data['properties'] = {'title': line['Category'],
					'description': line['Descript'],
					'date': line['Date']}
		data['geometry'] = { 'type': 'Point',
					'coordinates' : (line['X'], line['Y'])}

		# Add data dictionary to item_list
		item_list.append(data)

	# For each point in item_list, add it to a dictionary. Setdefault creates 
	# key: value of 'features': [] 
	# With each iteration, the point is being appended to that list		
	for point in item_list:
		geo_map.setdefault('features', []).append(point)

	# Data is now parsed in GeoJSON. Write to a file to upload to a gist. 
	# 'dumps' function prints geo_map dictionary into a GeoJSON file
	with open('file_sf.geojson', 'w') as f:
		f.write(geojson.dumps(geo_map))

def main():
	data = p.parse(p.MY_FILE, ",")

	return create_map(data)

if __name__ == '__main__':
	main()















