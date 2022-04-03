def sortedSquaredArray(array):
    new = [0 for _ in array]
    # print("ki bal", new)
    for i in range(len(array)):
        val = new[i] 
        new[i] = val * val
        
    new.sort()
    return new

print( sortedSquaredArray([1, 4, 9, 16, 25]))