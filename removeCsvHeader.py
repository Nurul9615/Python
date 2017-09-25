#! python3
# Remove header from all csv files

import csv
import os

os.makedirs('headerRemoved', exist_ok = True)

for csvFileName in os.listdir('.'): # Loop over all files
	if not csvFileName.endswith('.csv'):
		continue # skip non csv files
	print('Removing header from '+ csvFileName + '...')

	csvRows = []
	csvFileObj = open(csvFileName)
	readerObj = csv.reader(csvFileObj)
	for row in readerObj:
		if readerObj.line_num == 1:
			continue
		csvRows.append(row)
	csvFileObj.close()

	csvFileObj = open(os.path.join('headerRemoved', csvFileName), 'w', newline='')
	csvWriter = csv.writer(csvFileObj)
	for row in csvRows:
		csvWriter.writerow(row)
	csvFileObj.close()