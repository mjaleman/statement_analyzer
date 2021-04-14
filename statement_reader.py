import csv
import decimal

categories = {}
total = 0

def organize_into_dict(category, amount):
    if category not in categories:
        categories[category] = amount
    else:
        categories[category] += amount

with open('Discover-Statement-20210412.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
            pass
        string_to_dec = decimal.Decimal(row["Amount"])
        organize_into_dict(row["Category"], string_to_dec)
        total += string_to_dec
        line_count += 1

del categories["Payments and Credits"]

for key in categories:
    print(f'{key} : {categories[key]}')
print(total)
