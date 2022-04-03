def firstDuplicateValue(array):
    # Write your code here.
    first = []
    counts = {}
    for item in array:
        if item in counts:
            counts[item] += 1
            first.append(item)
        else:
            counts[item] = 1
    if not first:
        return -1
    else:
        return first[0]

print(firstDuplicateValue([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
