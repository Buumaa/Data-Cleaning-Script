import csv

with open('data.csv') as f:
    reader = csv.reader(f)
    cleaned = [row for row in reader if row]

with open('cleaned_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(cleaned)

print("Data cleaned.")