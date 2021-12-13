def collatz(number):
    if(number == 1):
        print('Equation complete!')
    elif (number % 2 == 0):
        number = number / 2
        print(str(number))
        collatz(number)
    elif (number % 2 == 1):
        number = 3 * number + 1
        print(str(number))
        collatz(number)


def start():
    print('Please enter any number to test the Collatz Sequence')
    try:
        userNum = int(input())
    except ValueError:
        print('Please select an integer.')
        userNum = start()
    return userNum


startingNumber = start()
print('You entered: ' + str(startingNumber))
collatz(startingNumber)
