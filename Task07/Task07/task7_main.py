"""TASK 7 - main program importing the milkrate module."""
import milkrate

rate = milkrate.rate_per_litre(4.2, 8.7)
print(f"Milk Rate: Rs {rate:.2f}")
print(f"Payment: Rs {milkrate.payout(10, 4.2, 8.7):.2f}")
