# function are defined by keyword 'def'
# by default function return none
# to return output use return statement

def greet_user(first, last):
    print(f"Hi {first} {last}!")
    print('Welcome abroad!')


# greet_user('Ariful', 'Hasan')

def square(num):
    return num ** 2


result = square(5)
print(result)

emojis = {
    ":)": "😀",
    ":(": "😔"
}


def emoji_converter(message):
    words = message.split(' ')
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


msg = input('> ')
res = emoji_converter(msg)
print(res)
