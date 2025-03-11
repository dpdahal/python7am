print("==============Welcome to laptop bazar =================")
print("1. Dell(Rs:20000) 2. Toshiba(Rs:30000) 3. Mac(Rs:50000)")
option = int(input("Enter your choice: "))
dell_price=0
toshiba_price=0
mac_price=0
product_name=""
quantity=0
if option==1:
    quantity = int(input("Enter the quantity: "))
    dell_price = 20000*quantity
    product_name="Dell"
elif option==2:
    quantity = int(input("Enter the quantity: "))
    toshiba_price = 30000*quantity
    product_name="Toshiba"
elif option==3:
    quantity = int(input("Enter the quantity: "))
    mac_price = 50000*quantity
    product_name="Mac"
else:
    print("Invalid choice")


print("========Deliver Option==========")
print("1. Home(Rs:1000) 2. Pick up (Free)")
delivery_option = int(input("Enter your choice: "))
delivery_price=0
if delivery_option==1:
    delivery_price=1000

print("========Packing Option==========")
print("1. Plastic Bag(Rs:1000) 2. Box(Rs:2000) 3. Gift Wrap(Rs:5000)")
p_option = int(input("Enter your choice: "))
p_price =0
if p_option==1:
    p_price=1000
elif p_option==2:
    p_price=2000
elif p_option==3:
    p_price=5000

total = dell_price+toshiba_price+mac_price
tax_amount=0
print("========Location=============")
print("1. KTM(Rs:13% tax) 2. Lalitpur(Rs:0 tax) 3. Bhaktapur(Rs:0 tax)")
location = int(input("Enter your choice: "))
if location==1:
    tax_amount = total*0.13



grand_total = total+delivery_price+p_price+tax_amount
print("==============Invoice================")
print("Product Name: ",product_name)
print("Quantity: ",quantity)
print("Total: ",total)
print("Delivery Price: ",delivery_price)
print("Packing Price: ",p_price)
print("Tax: ",tax_amount)
print("Grand Total: ",grand_total)
print("=====================================")