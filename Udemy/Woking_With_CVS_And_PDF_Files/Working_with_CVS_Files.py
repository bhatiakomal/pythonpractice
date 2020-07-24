import csv
#open the file
data=open('new-csv.csv')
#cvs.deader
csv_data=csv.reader(data)
#reformat it into a python object list of list
data_lines=list(csv_data)
#print(data_lines)
#print(data_lines[0])
print(len(data_lines))
for i in data_lines[:5]:
    print(i)