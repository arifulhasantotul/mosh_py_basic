languages = ['C', 'C++', 'C#', 'Python', 'JS', 'Java', 'PHP', 'Ruby', 'GO']
# list[index]
print(languages[0])
print(languages[1])
print(languages[3])
print(languages[-1])
print(languages[-2])
# list[startIndex : ] => data found from startIndex to lastIndex
print(languages[2:])  # Will print from 2nd index to last
# list[ : endIndex] => data found from 0 index to (endIndex - 1)
print(languages[:6])  # Will print from 0 index to (6-1) = 5th index
# list[startIndex : endIndex] => data found from startIndex to (endIndex - 1)
print(languages[2:6])  # Will print from 2nd index to (6-1) = 5th index
print(languages)

numbers = [1, 20, 2, 3, 8, 9, 15, 4, 5, 6, 17]
max_num = 0
for num in numbers:
    if num > max_num:
        max_num = num

print(max_num)



