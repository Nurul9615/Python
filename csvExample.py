#! python3

import csv

exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
for row in exampleReader:
	print('Row #' + str(exampleReader.line_num) + ' ' + str(row))

exampleData = list(exampleReader)
# print(exampleData)
print(exampleData[0][0])

outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam', 'eggs', 'turkey'])
outputFile.close()