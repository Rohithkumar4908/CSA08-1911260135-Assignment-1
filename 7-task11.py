"""TASK 11 - reading the rate card from a JSON configuration file."""
import json
from decimal import Decimal

with open("rates.json") as f:
    cfg = json.load(f)

base_rate = Decimal(cfg["base_rate"])
fat_step = Decimal(cfg["fat_step_value"])
snf_step = Decimal(cfg["snf_step_value"])

print("Base Rate:", base_rate)
print("Fat Step:", fat_step)
print("SNF Step:", snf_step)

fat, snf = Decimal("4.2"), Decimal("8.7")
rate = base_rate + (fat - Decimal("3.5")) * 4 * Decimal("1") * (fat_step / Decimal("0.4"))         + (snf - Decimal("8.5")) * 3 * (snf_step / Decimal("0.3"))
print("Milk Rate:", rate)
print("Payment:", rate * 10)
