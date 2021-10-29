
def add_numbers(numbers):
    """
    Ex. add_numbers([9, 5, 11, 6, 1, 15]) returns 47
    :param numbers: a list of numbers
    :return: the sum of all the numbers in the list
    """
    y = 0

    for x in numbers:
        y = y + x
    return y



def get_max(numbers):
    """
    Ex. get_max([45, 23, 99, 34, 67, 98, 0]) returns 99
    :param numbers: a list of numbers
    :return: The largest number in the list
    """
    y = numbers[0]
    for x in numbers:
        if x >= y:
            y = x
    return y


def get_min(numbers):
    """
    Ex. get_min([45, 23, 99, 34, 67, 98, 0]) returns 0
    :param numbers: a list of numbers
    :return: The smallest number in the list
    """
    y = numbers[0]
    for x in numbers:
        if x <= y:
            y = x
    print(y)
    return y


def merge(list1, list2):
    """
    Ex. merge([3, 4, 7, 9], [1, 5, 8, 11]) return [1, 3, 4, 5, 7, 8, 9, 11]
    :param list1: a list in sorted order
    :param list2: a second list in sorted order
    :return: a single list consisting of both smaller lists combined in sorted order.
    """
    list_two = []
    z = 0
    y = 0
    for x in range(len(list1 + list2)):
        if z >= len(list2):
            for x in range(len(list2)):
                list_two.append(list1[z])
                z = z + 1
            break
        if y >= len(list1):
            for x in range(len(list1)):
                list_two.append(list2[y])
                y = y + 1
            break

        if list1[z] >= list2[y]:
            list_two.append(list2[y])
            y = y + 1
        elif list1[z] <= list2[y]:
            list_two.append(list1[z])
            z = z + 1
        elif list1[z] == list2[y]:
            list_two.append(list1[z])
            z = z + 1
    print(list_two)
    return list_two



merge([3, 4, 7, 9], [1, 5, 8, 11])

