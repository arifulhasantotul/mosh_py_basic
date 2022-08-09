nums = [5, 7, 2, 6, 4, 5, 4, 2]
# list.append(el) - add element in the last
# nums.append(20)
# list.insert(index, el) - add element in the given index
# nums.insert(1, 20)
# list.remove(el) - removes first match element from the list
# nums.remove(5)
# list.clear() - removes all the element from list and return []
# nums.clear()
# list.pop() - removes the last element from list
# nums.pop()
# list.index(el) - returns the index position of an element
# print(nums.index(20))
# instead of list.index use below method, bcz it doesn't give any error if the element doesn't exist
# print(5 in nums)
# list.count(el) - returns total element number
# print(nums.count(5))
# list.sort() - sorts the list in ascending order
# nums.sort()
# list.reverse() - reverse the existing list
# nums.reverse()
# list.copy() - creates an independent list
# nums2 = nums.copy()
# print("nums2", nums2)
# nums.append(50)
# print("nums", nums)

# Que: Remove the duplicate items from a list
unique_nums = []
for el in nums:
    if el not in unique_nums:
        unique_nums.append(el)

print(unique_nums)

