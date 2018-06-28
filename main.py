import sys
import csv

reader = csv.reader(sys.stdin)
for i, line in enumerate(reader):
    if i < 7:
        continue

    if i == 7:
        line = ['company', 'department', 'jobtitle', 'lastname', 'email', 'zip', 'state', 'phone', line[8], line[9], 'fax', 'mobilephone', 'website']

    print(line)

