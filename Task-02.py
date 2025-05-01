# Task 2: Simple Bill Calculator

def bill_calculator():
    total = 0
    while True:
        item = input("Enter item name (or 'done' to finish): ")
        if item.lower() == 'done':
            break
        try:
            price = float(input(f"Enter price of {item}: "))
            quantity = int(input(f"Enter quantity of {item}: "))
            total += price * quantity
        except ValueError:
            print("Invalid input. Please enter numeric values for price and quantity.")
    
    gst = total * 0.18
    grand_total = total + gst

    print(f"\nSubtotal: ₹{total:.2f}")
    print(f"GST (18%): ₹{gst:.2f}")
    print(f"Total Bill: ₹{grand_total:.2f}")

# Run Task 2
bill_calculator()
