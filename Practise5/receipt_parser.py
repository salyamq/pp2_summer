import re
import json

with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Tasks:
# Extract all prices from the receipt
# Find all product names
# Calculate total amount
# Extract date and time information
# Find payment method
# Create a structured output (JSON or formatted text)

# ----------------------------------------

# Extract all prices from the receipt
prices = re.findall(r'Стоимость\s+(\d+(?: \d+)*(?:[.,]\d+)?)', text)
print(prices)

print("-" * 50)

# Find all product names
product_names = re.findall(r'\d+\.\s*\n(.+)', text)
print(product_names)

print("*" * 50)

# Calculate total amount
total_amount = 0
for price in prices:
    amount = re.sub(r"\s", "", price)
    amount = re.sub(r",", ".", amount)
    total_amount = total_amount + float(amount)
print(total_amount)

print("*" * 50)

# Extract date and time information
date = re.findall(r"\d{1,2}\.\d{1,2}\.\d{2,4}", text)
time = re.findall(r"\d{2}:\d{2}:\d{2}", text)
print(date, time)

print("*" * 50)

# Find payment method
payment_method = re.search(r"банковская карта|наличным|qr", text.lower())
print(payment_method)

# Create a structured output (JSON or formatted text)
output = dict()
output["products"] = list()

for product, price in zip(product_names, prices):
    output["products"].append({
        "product": product,
        "price": price
    })

output["date"] = date
output["time"] = time
output["payment_method"] = payment_method.group()
output["total_amount"] = total_amount

with open("structured_receipt.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=4)
print("done")









