def is_sorted(list1):
    for index in range(len(list1)-1):
        if list[index] > list1[index+1]:
            return True

    return False