# i = 1
# while i <= 5:
#     print('*' * i)
#     i += 1
# print("Done")

# secret_num = 7
# chances = 3
# guess_count = 0
# while guess_count < chances:
#     guess = input("Guess from (0-9): ")
#     guess_count += 1
#     if int(guess) == secret_num:
#         print("You win!")
#         break
# else:
#     # this else is works for while loop not for if condition
#     print("You lose!")

isStarted = False

while True:
    command = input('> ').lower()

    if command == 'start':
        if isStarted:
            print('Car already started....')
        else:
            print('Car started... ready to go')
            isStarted = True
    elif command == 'stop':
        if not isStarted:
            print('Car already stopped!')
        else:
            print('Car stopped')
            isStarted = False
    elif command == 'help':
        print(f" start - to start the car \n stop - to stop the car \n quit - to quit the game")
    elif command == 'quit':
        break
    else:
        print("I don't understand that....")