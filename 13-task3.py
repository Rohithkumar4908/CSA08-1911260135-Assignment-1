"""TASK 3 - variables and constants for the milk payment."""
BASE_RATE = 30.00      # rupees per litre at standard quality
FAT_STEP = 0.40        # rupees per 0.1% fat above standard
SNF_STEP = 0.30        # rupees per 0.1% SNF above standard

litres = 10.0
fat = 3.5
snf = 8.5

fat_steps = round((fat - 3.5) / 0.1)
snf_steps = round((snf - 8.5) / 0.1)
rate = BASE_RATE + fat_steps * FAT_STEP + snf_steps * SNF_STEP
payment = round(litres * rate, 2)

print("Milk Rate:", rate)
print("Total Payment:", payment)
