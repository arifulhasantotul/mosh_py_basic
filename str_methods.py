course = "Python for Beginners!"

print(len(course))  # length of str
print(course.upper())
# str.upper() = converting the str with uppercase but don't change the main string
print(course.lower())
# str.lower() = converting the str with lowercase but don't change the main string
print(course.find('y'))
# str.find() = case-sensitive method and returns the index of character. If char doesn't exist return -1
print(course.find('Beginners'))
# Return the first character index of the given words
print(course.replace('Beginners', 'absolute beginners'))
# str.replace() case-sensitive and replace the old characters to new characters
print('Python' in course)
# case-sensitive, checks for the characters exist in a variable returns boolean value
print(course)

