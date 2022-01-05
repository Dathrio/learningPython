spam = ["apples", "bananas", "tofu", "cats"]
eggs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def comma(list):
    for i in range(len(list)):
        if i == len(list) - 1:
            print("and " + str(list[i]))
            break
        print(str(list[i]) + ", ")


comma(spam)
comma(eggs)
