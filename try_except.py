try:
    age = int(input('age: '))
    income = 2000
    risk = income / age
    print(f" age {age} \n risk {risk}")
except ValueError:
    print('Invalid value')
except ZeroDivisionError:
    print('Age can not be 0')


