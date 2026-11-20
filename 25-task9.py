"""TASK 9 - automated tests for the milk payment calculator."""
from task6 import rate_per_litre, payout


def check(name, got, want):
    status = "PASS" if abs(got - want) < 0.001 else "FAIL"
    print(f"{name:28} expected {want:10.2f} got {got:10.2f} {status}")


check("normal 10, 3.5, 8.5", payout(10, 3.5, 8.5), 300.00)
check("higher 8.5, 4.2, 8.7", payout(8.5, 4.2, 8.7), 283.90)
check("lower 12, 3.1, 8.3", payout(12, 3.1, 8.3), 333.60)
check("min fat 10, 2.0, 8.5", payout(10, 2.0, 8.5), 240.00)
check("max fat 10, 7.0, 8.5", payout(10, 7.0, 8.5), 440.00)

# invalid input handling
try:
    float("ten")
    print("invalid text                  FAIL (no error raised)")
except ValueError:
    print("invalid text 'ten'            error raised as expected PASS")

litres = -5
print("negative litres rejected      PASS" if litres < 0 else "FAIL")

fat = 7.5
print("fat above 7.0 rejected        PASS" if not 2.0 <= fat <= 7.0 else "FAIL")
