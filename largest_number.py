def large(array):
    lar = -999
    new = 0
    for i in array:
        if i > lar:
            lar = i

            # return lar
    array.remove(lar)
    return array , lar
    
        

def findThreeLargestNumbers(array):
    new = []
    one,lar_one = large(array)
    new.append(lar_one)
    two,lar_two = large(one)
    new.append(lar_two)

    three,lar_three = large(two)
    new.append(lar_three)

    return sorted(new)

#   "array": [-1, -2, -3, -7, -17, -27, -18, -541, -8, -7, 7]

print(findThreeLargestNumbers([-1, -2, -3, -7, -17, -27, -18, -541, -8, -7, 7]))