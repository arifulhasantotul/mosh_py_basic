has_high_income = False
has_good_credit = True
has_criminal_record = False

if has_high_income and has_good_credit:
    print(f"Eligible for loan.")
elif has_high_income or has_good_credit:
    print(f"Can try for loan")

if has_good_credit and not has_criminal_record:
    print(f"Try for loan")
else:
    print(f"Not eligible")

full_name = input(f"Give your name: ")

if len(full_name) < 3:
    print(f"Name must be at least 3 characters!")
elif len(full_name) > 20:
    print(f"Name can be maximum of 20 characters!")
else:
    print(f"Name looks good!")

weight = input("Weight: ")
unit = input(f"(L)bs or (K)g: ")

if unit.upper() == 'K':
    print(f"You're {float(weight) * 2.20462} Kilograms")
elif unit.upper() == 'L':
    print(f"You're {float(weight) * 0.453592} Pounds")
else:
    print(f"For unit type 'L' or 'K'")
