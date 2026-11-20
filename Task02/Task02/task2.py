"""TASK 2 - values and types used in the milk payment system."""
from decimal import Decimal

farmer_id = 101
litres = 12.50
shift = "Morning"
paid = False

print(type(farmer_id))
print(type(litres))
print(type(shift))
print(type(paid))

print(7 / 2)    # normal division
print(7 // 2)   # floor division
print(7 % 2)    # remainder
print(0.1 + 0.2 == 0.3)          # float surprise
print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))  # Decimal is exact
