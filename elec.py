import sys

RATE_PER_UNIT = 5  # ₹5 per unit

if len(sys.argv) == 2:
    print("User provided units:")
    units = float(sys.argv[1])
else:
    print("No input given -- using default units:")
    units = 100   # default units

bill = units * RATE_PER_UNIT

print("Units Consumed:", units)
print("Rate Per Unit: ₹", RATE_PER_UNIT)
print("Total Electricity Bill: ₹", bill)
