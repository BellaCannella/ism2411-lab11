# AI USE: Explainer (asked to help explain the questions as well as
#         describing some steps I needed to take to make my code work)

print("---Reflection questions---")
#1. In a real-world situation I would use .get() in situations such as 
#   getting a customer's information (ex. phone number), because it may not
#   be listed. As for bracket notation, I would use that for information
#   that I'm confident exists such as the customer's name.

#2. Me personally, I don't know enough about excel to understand the similarities, 
#   but for the loop, python would be able to process much more information
#   compared to excel which makes it better for large datasets.

print("---Exercise 1 - One Customer---")

customer = {"name": "Isabella",
            "email": "icannella@usf.edu",
            "tier": "Gold",
            "ytd_spend": 1250}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

print("---Exercise 2 - Update and add---")

customer["phone"] = "4804509392"
print(customer)

customer["tier"] = "platinum"
print(customer)

del(customer["email"])
print(customer)

print("---Exercise 3 - Safe Lookup---")

print(customer.get("email", "no email on file"))

try:
    print(customer["email"])

except KeyError:
    print("KeyError: email does not exist")

print("---Exercise 4 - Iterate---")

for item in customer:
    print(item)

for key, value in customer.items():
    print(f"{key}:{value}")

# The difference between these two is that the regular for loop
# without .items() only prints the key, while the .items() command
# prints both the key and value.

print("---Exercise 5 - Lookup Table---")

tier_discounts = {"bronze": 0,
                  "silver": .05,
                  "gold": .10,
                  "platinum": .15}

customer.get("tier", "item")
customer.get("item")

discount_rate = tier_discounts.get(customer["tier"],0)
discount_amount = 200 * discount_rate
final_price = 200 - discount_amount 

print(f"Tier: {customer['tier']}")
print(f"Discount: {discount_rate:.0%}")
print(f"Final price: ${final_price:.2f}")

print("---Exercise 6 - List of dicts---")

dict1 = {"name": "Isabella", "tier": "gold"}
dict2 = {"name": "Alex", "tier": "silver"}
dict3 = {"name": "Jordan", "tier": "platinum"}


customers = [dict1, dict2, dict3]

purchase_price = 300

for customer in customers:
    name = customer["name"]
    tier = customer["tier"]
    
    discount_rate = tier_discounts.get(tier.lower(), 0)

    discount_amount = purchase_price * discount_rate

    print(f"{name} | {tier} | Discount: ${discount_amount:.2f}")

print("---Exercise 7 - Nested Catalog---")

catalog = {"Widget A": {"price": 9.99, "stock": 150},
           "Gadget C": {"price": 49.99, "stock": 8}}


for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product}") 

print("---Exercise 8 - Sales by region---")

transactions = [{"region": "South", "amount": 300},
                {"region": "North", "amount": 150},
                {"region": "South", "amount": 200}]

summary = {}

for transaction in transactions:

    region = transaction["region"]
    amount = transaction["amount"]

    summary[region] = summary.get(region, 0) + amount

for region in sorted(summary):
    print(f"{region}: {summary[region]}")

