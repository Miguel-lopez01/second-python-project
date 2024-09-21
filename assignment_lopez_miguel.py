item_1 = 30.00
item_2 = 40.00
item_3 = 50.00

item_total = item_1 + item_2 + item_3

def calculate_total_cost(prices):
    return sum(prices)

def apply_discount(total):
    if total >= 100:
        discount = total * 0.10  
        total_after_discount = total - discount
        print(f"10% discount applied: ₱{discount:.2f}")
    else:
        discount = 0
        total_after_discount = total
        print("No discount applied.")
    
    return total_after_discount

def calculate_loyalty_points(total):
    return total // 10  

def checkout():
    
    item_1 = 30.00
    item_2 = 40.00
    item_3 = 50.00
    
    item_prices = [item_1, item_2, item_3]
    total_cost = calculate_total_cost(item_prices)
    print(f"Total cost before discount: ₱{total_cost:.2f}")
    
    final_total = apply_discount(total_cost)
    print(f"Total cost after discount: ₱{final_total:.2f}")

    loyalty_points = calculate_loyalty_points(final_total)
    print(f"Loyalty points earned: {loyalty_points}")
 
    payment = 120.00
    print(f"Payment: ₱{payment:.2f}")
    
    if payment >= final_total:
        change = payment - final_total
        print(f"Payment accepted. Your change is: ₱{change:.2f}")
    else:
        print("Payment is less than the total amount. Please try again.")
        
checkout()
