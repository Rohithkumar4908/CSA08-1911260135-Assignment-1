"""TASK 7 - milkrate module: rate and payment functions."""

BASE_RATE = 30.00


def rate_per_litre(fat, snf):
    """Rate for one litre given fat and SNF percentages."""
    return round(BASE_RATE + (fat - 3.5) * 4 + (snf - 8.5) * 3, 2)


def payout(litres, fat, snf):
    """Payment for one milk entry."""
    return round(litres * rate_per_litre(fat, snf), 2)


if __name__ == "__main__":
    demo = [(10, 3.5, 8.5), (8.5, 4.2, 8.7), (12, 3.1, 8.3)]
    for litres, fat, snf in demo:
        print(f"Litres: {litres}, Rate: {rate_per_litre(fat, snf):.2f}, "
              f"Payment: {payout(litres, fat, snf):.2f}")
