#!/usr/bin/python3

def printTable(tableData):
# Get the maximum length of each column
	colWidths = [max([len(item) for item in col]) for col in tableData]
# Transpose the table data
tableDataTransposed = zip(*tableData)
# Print the table
for row in tableDataTransposed:
	for i in range(len(row)):
		print(row[i].rjust(colWidths[i]), end=' ')
		print()
tableData = [['apples', 'oranges', 'cherries', 'banana'], 
	     ['Alice', 'Bob', 'Carol', 'David'], 
	     ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
