def check_sum(values):
    total = 0
    cumsum = []
    for num in values:
        total += num
        cumsum.append(total)
    return cumsum

