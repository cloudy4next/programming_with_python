
# returns the major item is greater than divisable by 2 of nums
def majority(nums):
    half = len(nums)//2
    print(half)
    counts = {}
    for item in nums:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    for k,v in counts.items():
        if v > half:
            return k

nums = [3,2,3,2,3,4,2,2,2]
result =majority(nums)
print(result)
