demo_course = "I'm a student"
course = 'Python Course for "Beginners"'
# index = 0123456789

email = '''
    Hi XXX,
    How are you doing.
'''
print(course[0])  # getting 1st character
print(course[1])  # getting 2nd character
print(course[-1])  # getting last character
print(course[-2])  # getting 2nd last character

# course[startIndex : lastIndex]
print(course[0:])  # getting character from 1st to last
print(course[2:])  # getting character from 3rd to last
print(course[1:5])  # getting character from 2nd to (5-1)=4th
print(course[1:6])  # getting character from 2nd to (6-1)=5th
print(course[:6])  # getting character from 1st to (6-1)=5th
print(course[:])  # getting character from 1st to last
print(course[1:-1])  # getting character from 2nd to (-1-1)= 2nd last character

