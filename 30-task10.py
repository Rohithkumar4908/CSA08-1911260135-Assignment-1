"""TASK 10 - float vs Decimal over 300, 6000 and 150000 payments."""
import time
from decimal import Decimal, ROUND_HALF_UP

COUNTS = [300, 6000, 150000]
rate_f = 33.40
rate_d = Decimal("33.40")
litres = 8.5

for n in COUNTS:
    t0 = time.perf_counter()
    total_f = 0.0
    for _ in range(n):
        total_f += litres * rate_f
    t1 = time.perf_counter()
    total_d = Decimal("0")
    for _ in range(n):
        total_d += Decimal("8.5") * rate_d
    t2 = time.perf_counter()
    print(f"{n:>7} payments | float total {total_f:.4f} ({(t1 - t0) * 1000:.1f} ms) | "
          f"Decimal total {total_d} ({(t2 - t1) * 1000:.1f} ms)")

# rounding policy: per payment vs final total
per = Decimal("10.005").quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
per_payment = per * 3
final_only = (Decimal("10.005") * 3).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
print("round each payment:", per_payment, "| round final total:", final_only)
