def nested_sum(list_of_integers):
    sum_of_integers = 0
    for number in list_of_integers:
        for nested in number:
            sum_of_integers += nested

    print(sum_of_integers)

nested_sum([[1,2],[3,4],[5,23]])
