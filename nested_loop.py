for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")

# nums = [5, 2, 5, 2, 2]
nums = [2, 2, 2, 2, 5]
# for num in nums:
#     print(f"{'X' * num}")


for x_count in nums:
    output = ''
    for count in range(x_count):
        output += 'X'
    print(output)
    