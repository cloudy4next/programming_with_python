
# returns false if item is duplicate
def find_duplicate(nums):
    duplicate = False
    counts = {}
    for item in nums:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    for k,v in counts.items():
        if v > 1:
            duplicate = True
    return duplicate
nums = [2,14,18,22,22]

result =find_duplicate(nums)
print(result)
