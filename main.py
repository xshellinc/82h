import sys
import csv

a = input("Select contact owner")
print(a)

for i, line in enumerate(sys.stdin):
    if i < 6:
        continue

    print(line)

