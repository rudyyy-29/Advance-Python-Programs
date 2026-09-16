import csv 

with open('data.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['Hrishi', 19, 'Jalgoan'])
    writer.writerow(['Paresh', 19, 'Satara'])
    writer.writerow(['CharDiwari', 35, 'Mumbai'])
    writer.writerow(['Rudra', 20, 'Pune'])

    with open('data.csv','r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

import json

data=[{"Name": "Hrishi", "Age": 19, "City": "Jalgoan"},
      {"Name": "Paresh", "Age": 19, "City": "Satara"},
      {"Name": "CharDiwari", "Age": 35, "City": "Mumbai"},
      {"Name": "Rudra", "Age": 20, "City": "Pune"}]

with open('data.json', 'w') as file:
    json.dump(data, file)

print("CSV data successfully converted to JSON.")