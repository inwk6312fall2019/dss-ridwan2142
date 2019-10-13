def middle(new_list):
    value = new_list[:]
    del value[0]
    del value[len(value)-1]
    print(value)

middle([1,3,6])