# Smart Canteen Billing and Order Analyzer

print("\n========== SMART CANTEEN ==========")
print("""
1. Veg Sandwich - ₹60
2. Masala Dosa - ₹80
3. Chole Rice - ₹90
4. Paneer Roll - ₹100
5. Tea - ₹20 
6. Exit""")
receipt = []
discount = 0
subtotal = 0
while True:
    user = int(input("Choose item number: "))
    quantity = int(input("Enter quantity: "))
    
    if user == 1:
        amount = 60 * quantity
        print(f"Added: Veg Sandwich x {quantity} = ₹{amount}")
        receipt.append(f"Veg Sandwich x {quantity}: ₹{amount}")
        re_order = input("Add another item? (y/n): ")
        subtotal += amount
        if re_order.lower() == 'y':
            continue
        elif re_order.lower() == 'n':
            break
        
    elif user == 2:
        amount = 80 * quantity
        print(f"Added: Masala Dosa x {quantity} = ₹{amount}")
        receipt.append(f"Masala Dosa x {quantity}: ₹{amount}")
        re_order = input("Add another item? (y/n): ")
        subtotal += amount
        if re_order.lower() == 'y':
            continue
        elif re_order.lower() == 'n':
            break

    elif user == 3:
        amount = 90 * quantity
        print(f"Added: Chole Rice x {quantity} = ₹{amount}")  
        receipt.append(f"Chole Rice x {quantity}: ₹{amount}")
        re_order = input("Add another item? (y/n): ")
        subtotal += amount
        if re_order.lower() == 'y':
            continue
        elif re_order.lower() == 'n':
            break

    elif user == 4:
        amount = 100 * quantity
        print(f"Added: Paneer Roll x {quantity} = ₹{amount}")
        receipt.append(f"Paneer Roll x {quantity}: ₹{amount}")
        subtotal += amount
        re_order = input("Add another item? (y/n): ")
        if re_order.lower() == 'y':
            continue
        elif re_order.lower() == 'n':
            break
        
    elif user == 5:
        amount = 20 * quantity
        print(f"Added: Tea x {quantity} = ₹{amount}")
        receipt.append(f"Tea x {quantity}: ₹{amount}")
        subtotal += amount
        re_order = input("Add another item? (y/n): ")
        if re_order.lower() == 'y':
            continue
        elif re_order.lower() == 'n':
            break
    elif user == 6:
        print("Thank you for visiting the Smart Canteen!")
        break
    else:
        print("Invalid item number. Please choose a valid option.")

final_total = subtotal - discount

print("\n========== RECEIPT ==========")
for item in receipt:
    print(item)

print("-----------------------------")
print(f"Subtotal: Rs.{subtotal}")
print(f"Discount: Rs.{discount}")
print(f"Final total: Rs.{final_total}")
print("=============================")
print("Thank you!")