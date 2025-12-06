# Problem 1 – quantity, price, 10% discount over 10000

def comp_ext_price(qty, unitprice):
    ext_price = qty * unitprice
    if ext_price > 10000:
        disc_amt = ext_price * 0.10
    else:
        disc_amt = 0
    new_ext_price = ext_price - disc_amt
    return new_ext_price


total_ext_price = 0.0

response = input("Do you want to do this program? Enter Yes or No: ")

while response.lower() == "yes":
    qty = float(input("Enter quantity: "))
    price = float(input("Enter price: "))

    total = comp_ext_price(qty, price)
    print(f"Qty: {qty}, Price: ${price:.2f}, Total: ${total:.2f}")

    total_ext_price += total
    response = input("Do you want to do this program again? Enter Yes or No: ")

print(f"Sum of all totals: ${total_ext_price:.2f}")
