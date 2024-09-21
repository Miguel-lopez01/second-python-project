item_1 = 30.00
item_2 = 40.00
item_3 = 50.00

item_total = item_1 + item_2 + item_3

print(f"Total cost before any discount: ₱{item_total:.2f}")

if item_total >= 100:
    dis = item_total * 0.10
    print(f"10% discount is applied: ₱{dis:.2f}")

    finaltotal = item_total - dis
    loy = finaltotal / 10

    print(f"The final price after discount is: ₱{finaltotal:.2f}")
    print(f"Loyalty points earned: ₱{loy:.2f}")

price = 120.00
payment = price

if payment >= finaltotal:
    change = payment - finaltotal
    print(f"Payment accepted. Your change is: ₱{change:.2f}")
else:
    print("Payment is less than the total amount. Please try again.")
