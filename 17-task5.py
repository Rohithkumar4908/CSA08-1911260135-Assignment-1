"""TASK 5 - reading and validating milk collection input."""

def read_float(prompt):
    raw = input(prompt).strip()
    try:
        value = float(raw)
    except ValueError:
        return None
    return value

litres = read_float("Enter milk quantity: ")
fat = read_float("Enter fat percentage: ")
snf = read_float("Enter SNF percentage: ")

if litres is None or fat is None or snf is None:
    print("Invalid input - numbers only, please re-enter.")
elif litres < 0:
    print("Invalid input - quantity cannot be negative.")
else:
    rate = 30.00 + round((fat - 3.5) * 4, 2) + round((snf - 8.5) * 3, 2)
    amount = round(litres * rate, 2)
    print("MILK PAYMENT DETAILS")
    print("-" * 25)
    print(f"Litres :  {litres:.2f}")
    print(f"Fat     :  {fat:.2f}")
    print(f"SNF     :  {snf:.2f}")
    print(f"Rate    :  Rs {rate:.2f}")
    print(f"Amount :  Rs {amount:.2f}")
