# Lab 6 - Data Structures and CSV Files (Coding Cafe)
# Run from this folder; expects data/menu.csv and data/monsoon_sales.csv next to it.

# ---------- 1. Lists ----------
print("== Lists ==")
orders = ["masala chai", "samosa", "bun maska", "filter coffee"]
print("First order:", orders[0])
print("Last order:", orders[-1])
print("Positions 1 and 2:", orders[1:3])
print("Number of orders:", len(orders))
backup = orders.copy()
orders.append("cookie")
print("Orders:", orders)
print("Backup:", backup)

# Guided practice 1
orders = ["chai", "maggi", "chai"]
print("type:", type(orders))
print("first item:", orders[0])
print("last item:", orders[-1])
print("first two items:", orders[:2])
print("number of items:", len(orders))

# Guided practice 2
orders.append("samosa")
orders.extend(["coffee", "cookie"])
orders.insert(1, "puff")
orders[1] = "veg puff"
print(orders)

# Guided practice 3
print("chai count:", orders.count("chai"))
print("veg puff position:", orders.index("veg puff"))
served = orders.pop(0)
if "cookie" in orders:
    orders.remove("cookie")
orders.sort()
print("served:", served)
print("remaining:", orders)

# Your turn: order queue
orders = ["chai", "maggi", "chai", "samosa"]
orders.append("brownie")
orders.extend(["coffee", "cookie"])
orders.insert(1, "puff")
orders.remove("cookie")
served = orders.pop(0)
print("Served:", served)
print("Orders left:", len(orders))
print("Chai orders left:", orders.count("chai"))
saved = orders.copy()
saved.sort()
print("Saved (sorted):", saved)
orders.clear()
print("Orders after clearing:", orders)

# ---------- 2. Sets ----------
print("\n== Sets ==")
morning = set(["Asha", "Ravi", "Asha", "Meera"])
evening = {"Ravi", "Kabir", "Meera", "Tara"}
print("Morning guests:", sorted(morning))
print("Union:", sorted(morning.union(evening)))
print("Intersection:", sorted(morning.intersection(evening)))
print("Difference:", sorted(morning.difference(evening)))
print("Symmetric difference:", sorted(morning ^ evening))
print("Is 'Zoya' in morning?", "Zoya" in morning)

# Guided practice 1
bookings = ["Asha", "Ravi", "Asha", "Meera"]
lakeside = set(bookings)
lakeside.add("Zoya")
lakeside.update(["Kabir", "Asha"])
lakeside.discard("Ravi")
print("Lakeside:", sorted(lakeside))

# Guided practice 2
hilltop = {"Meera", "Tara"}
everyone = lakeside.union(hilltop)
both = lakeside.intersection(hilltop)
lakeside_only = lakeside.difference(hilltop)
one_area = lakeside.symmetric_difference(hilltop)
print("everyone:", sorted(everyone))
print("both:", sorted(both))
print("Lakeside only:", sorted(lakeside_only))
print("exactly one area:", sorted(one_area))
print("both is a subset of Hilltop:", both.issubset(hilltop))
print("Tara at Lakeside:", "Tara" in lakeside)

# Your turn: festival guest lists
lakeside_bookings = ["Asha", "Ravi", "Meera", "Asha", "Kabir"]
hilltop_bookings = ["Meera", "Kabir", "Ishaan", "Tara", "Meera"]
lakeside = set(lakeside_bookings)
hilltop = set(hilltop_bookings)
lakeside.add("Zoya")
lakeside.discard("Ravi")
print("Total unique guests:", len(lakeside.union(hilltop)))
print("Both areas:", sorted(lakeside.intersection(hilltop)))
print("Lakeside only:", sorted(lakeside.difference(hilltop)))
print("Exactly one area:", sorted(lakeside.symmetric_difference(hilltop)))
print("Subset check:", lakeside.intersection(hilltop).issubset(lakeside))

# ---------- 3. Tuples ----------
print("\n== Tuples ==")
recipe = ("Masala Chai", 40, 4)
name, price, prep_mins = recipe
print(f"{name} costs Rs {price} and takes {prep_mins} minutes")
print("Count of 40:", recipe.count(40))
print("Position of 40:", recipe.index(40))

recipe = ("Masala Chai", 40, 4)
item_name, item_price, prep_time = recipe
print("item:", item_name, "| price:", item_price)
print("prep time:", prep_time)
print("count of 40:", recipe.count(40))
print("position of 4:", recipe.index(4))
print("first field:", recipe[0])

# ---------- 4. Dictionaries ----------
print("\n== Dictionaries ==")
menu_prices = {"Chai": 40, "Samosa": 30, "Bun Maska": 50}
print("Chai price:", menu_prices["Chai"])
print("Cold coffee price:", menu_prices.get("Cold Coffee", 0))
menu_prices["Cold Coffee"] = 70
menu_prices["Chai"] = 45
for item, price in menu_prices.items():
    print(f"{item}: Rs {price}")

# Guided practice 1
prices = {"Chai": 40, "Samosa": 30}
print("chai:", prices["Chai"])
print("pizza price:", prices.get("Pizza", 0))
prices["Chai"] = 45
prices["Puff"] = 45
removed = prices.pop("Samosa")
print("removed:", removed)
print("prices now:", prices)

# Guided practice 2
prices = {"Chai": 45, "Brownie": 90, "Puff": 45}
order = {"Chai": 4, "Brownie": 2}
print("keys:", list(prices.keys()))
print("values:", list(prices.values()))
bill = 0
for item, qty in order.items():
    bill += prices[item] * qty
print("bill:", bill)
if bill > 300:
    bill = bill * 0.9
print("payable:", bill)

# Guided practice 3
orders_today = ["chai", "coffee", "chai", "samosa"]
counts = {}
for item in orders_today:
    counts[item] = counts.get(item, 0) + 1
print("counts:", counts)
print("most ordered:", max(counts, key=counts.get))

# Your turn: festival order
prices = {"Masala Chai": 40, "Samosa": 30, "Chocolate Brownie": 90, "Veg Puff": 45}
stock = {"Masala Chai": 10, "Samosa": 4, "Chocolate Brownie": 8, "Veg Puff": 0}
order = {"Masala Chai": 3, "Samosa": 2, "Chocolate Brownie": 1, "Veg Puff": 2}
prices["Lemonade"] = 60
prices["Samosa"] = 35
prices.pop("Lemonade")
bill = 0
for item, qty in order.items():
    bill += prices[item] * qty
payable = bill * 0.9 if bill > 300 else bill
unavailable = []
for item, qty in order.items():
    if qty > stock.get(item, 0):
        unavailable.append(item)
    else:
        stock[item] -= qty
print("Bill:", bill)
print("Payable:", payable)
print("Unavailable:", unavailable)
print("Stock:", stock)

# ---------- 5. CSV ----------
print("\n== CSV ==")
menu_prices = {}
with open("data/menu.csv") as f:
    next(f)
    for line in f:
        item, category, price, prep_min, vegetarian = line.strip().split(",")
        menu_prices[item] = int(price)
print("Items loaded:", len(menu_prices))
print("Masala Chai price:", menu_prices["Masala Chai"])
print("Filter Coffee price:", menu_prices["Filter Coffee"])

sales = []
with open("data/monsoon_sales.csv") as f:
    columns = next(f).strip().split(",")
    for line in f:
        values = line.strip().split(",")
        row = dict(zip(columns, values))
        row["qty"] = int(row["qty"])
        sales.append(row)
units_sold = {}
for row in sales:
    units_sold[row["item"]] = units_sold.get(row["item"], 0) + row["qty"]
print("rows loaded:", len(sales))
print("Masala Chai units:", units_sold["Masala Chai"])
print("Chicken Roll units:", units_sold["Chicken Roll"])

# ---------- 6. Capstone: festival report ----------
print("\n== Festival report ==")
report = {}
for row in sales:
    item = row["item"]
    entry = report.setdefault(item, {"qty_sold": 0, "revenue": 0})
    entry["qty_sold"] += row["qty"]
    entry["revenue"] += row["qty"] * menu_prices[item]
ranked = sorted(report.items(), key=lambda pair: pair[1]["revenue"], reverse=True)
print("item,qty_sold,revenue")
for item, data in ranked:
    print(",".join([item, str(data["qty_sold"]), str(data["revenue"])]))
print("Items in report:", len(report))

# ---------- 7. Capstone: loyalty list ----------
print("\n== Loyalty list ==")
customers = {}
for row in sales:
    cust = row["customer_id"]
    if not cust:
        continue
    c = customers.setdefault(cust, {"orders": set(), "items": set(), "spend": 0})
    c["orders"].add(row["order_id"])
    c["items"].add(row["item"])
    c["spend"] += row["qty"] * menu_prices[row["item"]]

qualifying = [cid for cid, c in customers.items() if len(c["orders"]) >= 2]
print("Qualifying customers:", len(qualifying))
top = max(customers, key=lambda cid: customers[cid]["spend"])
print("Highest spender:", top, customers[top]["spend"])
print("Both C01 and C02:", sorted(customers["C01"]["items"].intersection(customers["C02"]["items"])))
print("Only C01:", sorted(customers["C01"]["items"].difference(customers["C02"]["items"])))
cards = [(cid, len(c["orders"]), len(c["items"]), c["spend"]) for cid, c in customers.items()]
cards.sort(key=lambda row: (-row[3], row[0]))
print("Top five:")
for card in cards[:5]:
    print(card)
