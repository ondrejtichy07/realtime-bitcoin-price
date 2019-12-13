from datetime import datetime
import requests
import json
import time
import csv

url = 'https://blockchain.info/ticker'
i = 0

fieldnames = ["x_value", "y_value"]

with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:
    r = requests.get(url)
    data = r.json()
    price = data["USD"]["buy"]
    x_value = datetime.now().strftime('(%d.%m.%y) %H:%M')
    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "x_value": x_value,
            "y_value": price
        }

        csv_writer.writerow(info)
        print(price, x_value)

    time.sleep(60)
