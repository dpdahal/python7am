print("==============Computer Bazar =========")
print("1. Dell(Rs:20000) 2. Mac(50000) 3. Toshiba(30000)")
option = int(input("Select any option: "))

dell_price = 0
mac_price = 0
toshiba_price = 0
total_qt = 0

if option == 1:
    qt = int(input("Enter qt: "))
    total_qt += qt
    dell_price += 20000 * qt

elif option == 2:
    qt = int(input("Enter qt: "))
    total_qt += qt
    mac_price += 50000 * qt

elif option == 3:
    qt = int(input("Enter qt: "))
    total_qt += qt
    toshiba_price += 30000 * qt


else:
    print("Invalid option")
    exit()

print("Delivery option: 1. Home(1000) 2. Pickup(free)")
dop = int(input("Enter option: "))

delivery_price = 0

if dop == 1:
    delivery_price += 1000

print("Packing: 1. Plastic(500) 2. Bag(1000) 3. Gift box(5000) 4. None")
pot = int(input("Enter option: "))
plastic_price = 0
bag_price = 0
git_price = 0

if pot == 1:
    plastic_price += 500
elif pot == 2:
    bag_price += 1000

elif pot == 3:
    git_price += 5000

elif pot == 4:
    pass
else:
    print("invalid option")

print("Location: 1. ktm (13%) 2. Ltp 3. Bkt")
lop = int(input("Selection location: "))
tax_amount = 0

total_amount = dell_price + mac_price + toshiba_price

if lop == 1:
    tax_amount += total_amount * 0.13

gt_price = tax_amount + total_amount + delivery_price + plastic_price + bag_price + git_price

print(f"Total Price: {total_amount}")
print(f"Total qt: {total_qt}")
print(f"Tax Amount: {tax_amount}")
print(f"GT Amount: {gt_price}")
