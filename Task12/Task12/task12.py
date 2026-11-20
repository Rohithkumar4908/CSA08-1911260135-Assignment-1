"""TASK 12 - revised design: seasonal rates, two-decimal readings, bonus."""
from decimal import Decimal, ROUND_HALF_UP

SEASONS = {
    "normal": (Decimal("30.00"), Decimal("0.40")),
    "summer": (Decimal("32.00"), Decimal("0.45")),
}
SNF_STEP = Decimal("0.30")
BONUS_LIMIT = Decimal("500")
BONUS_PER_LITRE = Decimal("0.50")


def rate_per_litre(fat, snf, season="normal"):
    base, fat_step = SEASONS[season]
    fat_steps = int(((fat - Decimal("3.5")) / Decimal("0.1")).quantize(
        Decimal("1"), rounding=ROUND_HALF_UP))
    snf_steps = int(((snf - Decimal("8.5")) / Decimal("0.1")).quantize(
        Decimal("1"), rounding=ROUND_HALF_UP))
    return base + fat_steps * fat_step + snf_steps * SNF_STEP


def ten_day_total(entries, season="normal"):
    total_qty = sum(e[0] for e in entries)
    subtotal = sum(e[0] * rate_per_litre(e[1], e[2], season) for e in entries)
    bonus = total_qty * BONUS_PER_LITRE if total_qty > BONUS_LIMIT else Decimal("0")
    return subtotal + bonus, bonus


entries = [(Decimal("200"), Decimal("3.5"), Decimal("8.5")),
           (Decimal("200"), Decimal("4.2"), Decimal("8.7")),
           (Decimal("150"), Decimal("3.5"), Decimal("8.5"))]

for season in ("normal", "summer"):
    total, bonus = ten_day_total(entries, season)
    print(f"Season: {season}  Bonus: Rs {bonus}  Total Payment: Rs {total}")

# test table
tests = [("normal", 400, Decimal("0")), ("summer", 400, Decimal("0")),
         ("normal", 500, Decimal("0")), ("summer", 550, Decimal("275.00")),
         ("normal", 550, Decimal("275.00")), ("summer", 600, Decimal("300.00"))]
print()
for season, qty, want in tests:
    e = [(Decimal(qty), Decimal("3.5"), Decimal("8.5"))]
    _, bonus = ten_day_total(e, season)
    print(f"{season:7} {qty} litres -> bonus {bonus} expected {want} "
          f"{'PASS' if bonus == want else 'FAIL'}")
