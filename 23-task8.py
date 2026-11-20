"""TASK 8 - milk payment algorithm implemented and hand-traced."""

BASE_RATE = 30.00
FAT_STEP = 0.40
SNF_STEP = 0.30


def rate(fat, snf):
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)
    return round(BASE_RATE + fat_steps * FAT_STEP + snf_steps * SNF_STEP, 2)


def payment(litres, fat, snf):
    return round(litres * rate(fat, snf), 2)


entries = [(10, 3.5, 8.5), (8.5, 4.2, 8.7), (12, 3.1, 8.3)]
total = 0
for litres, fat, snf in entries:
    p = payment(litres, fat, snf)
    total += p
    print(f"Payment: Rs {p:.2f}")
print(f"Ten-Day Total: Rs {total:.2f}")
