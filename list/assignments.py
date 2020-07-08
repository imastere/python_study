def assignment4_3():
    numbers = list(range(1, 21))
    for num in numbers:
        print(num)


def assignment4_4():
    numbers = list(range(1, 1000001))
    for num in numbers:
        print(num)


def assignment4_5():
    numbers = list(range(1, 1000001))
    print(max(numbers))
    print(min(numbers))
    print(sum(numbers))


def assignment4_6():
    numbers = list(range(1, 21, 2))
    for num in numbers:
        print(num)


def assignment4_7():
    numbers = [value * 3 for value in range(1, 11)]
    for num in numbers:
        print(num)


def assignment4_8():
    numbers = list(range(1, 11))
    for num in numbers:
        print(num ** 3)


def assignment4_9():
    numbers = [value ** 3 for value in range(1, 11)]
    for num in numbers:
        print(num)


def assignment4_10():
    letters = ['a', 'b', 'c', 'd', 'e', 'f','g']
    print("The first three items in the list are")
    print(letters[1:3])
    print("Three items from the middle of the list are")
    print(letters[int(len(letters)/2-1):int(len(letters)/2+2)])
    print("The last three items in the list are")
    print(letters[-3:])

def assignment4_11():
    pizzas = ['pizza1','pizza2']
    friend_pizzas = pizzas[:]
    pizzas.append('pizza3')
    friend_pizzas.append('pizza4')
    print("My favorite pizzas are:")
    print(pizzas)
    print("My friend's favorite pizzas are:")
    print(friend_pizzas)

if __name__ == '__main__':
    assignment4_11()
