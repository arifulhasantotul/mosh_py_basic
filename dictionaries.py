customer = {
    "name": "Jon smith",
    "age": 30,
    "is_verified": True
}
# getting value: use get method to get value from dictionaries
# value = customer["name"]
value = customer.get("name")
# value = customer["birthday"]
# value = customer.get("birthday")
# value = customer.get("birthday", "01 Jan 1998")

# adding value:
customer["dob"] = '27 March 1998'
# print(value)
# print(customer)

phone = input('phone: ')
digits = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five"
}
for num in phone:
    print(digits.get(num))


