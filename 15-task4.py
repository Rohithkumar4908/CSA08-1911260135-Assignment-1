"""TASK 4 - expressions: milk rate and payment from fat and SNF."""
base = 30.00
litres = 10.0
fat, snf = 4.2, 8.7

fat_adjust = round((fat - 3.5) * 4, 2)    # 0.40 per 0.1 -> x4 per 1.0
snf_adjust = round((snf - 8.5) * 3, 2)    # 0.30 per 0.1 -> x3 per 1.0
rate = round(base + fat_adjust + snf_adjust, 2)
total = round(rate * litres, 2)

print("Fat Adjustment:", fat_adjust)
print("SNF Adjustment:", snf_adjust)
print("Milk Rate:", rate)
print("Total Payment:", total)
