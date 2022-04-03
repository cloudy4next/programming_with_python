from tkinter.messagebox import askretrycancel


def binarySearch(array, target):
    index = 0
    # new = -1
    # print(len(array))
    # for i in range(len(array)):
    #     if array[i] != target:
    #         # print(array[i])
    #         index = array[i]
    #     else:
    #         return -1
    # return index
    if target in array:
        return array.index(target)
    else:
        return -1
    # Write your code

print(binarySearch([0,1,21, 33, 45, 45, 61, 71, 72, 73],33))