import json
import csv
import redis


product_sales = {}
category_sales = {}

product_category = {}

with open("product.json", "r") as fin:
    product_info = json.load(fin)
    for info in product_info:
        product_category[info["product_id"]] = info["category"]

print(product_category)

with open("sales.csv", "r") as fin:
    reader = csv.DictReader(fin)
    for line in reader:
        product_id = int(line["product_id"])

        if product_id in product_category:
            category = product_category[product_id]
            if category not in category_sales:
                category_sales[category] = 0
            category_sales[category] += int(line["quantity"])
        else:
            print(f"Category for product [{product_id}] is unknown")


client = redis.Redis(host="127.0.0.1", port=6379)

for key, value in category_sales.items():
    client.set(f"category-{key}", value)