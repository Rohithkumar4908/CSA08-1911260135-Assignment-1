"""TASK 6 - the milk payment calculation split into functions."""

BASE_RATE = 30.00   # global constant


def rate_per_litre(fat, snf):
    """Return the rate for one litre from fat and SNF percentages."""
    return round(BASE_RATE + (fat - 3.5) * 4 + (snf - 8.5) * 3, 2)


def payout(litres, fat, snf):
    """Return the payment for one milk entry."""
    return round(litres * rate_per_litre(fat, snf), 2)


def ten_day_total(entries):
    """Return the total payment for a list of (litres, fat, snf)."""
    total = 0
    for litres, fat, snf in entries:
        total += payout(litres, fat, snf)
    return round(total, 2)


if __name__ == "__main__":
    entries = [(10, 3.5, 8.5), (8.5, 4.2, 8.7), (12, 3.1, 8.3)]
    for litres, fat, snf in entries:
        r = rate_per_litre(fat, snf)
        print(f"Litres: {litres}  Rate: Rs {r:.2f}  Payment: Rs {payout(litres, fat, snf):.2f}")
    print(f"Total Payment: Rs {ten_day_total(entries):.2f}")
