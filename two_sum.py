# two_sum.py
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# Input from userS
nums = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter target sum: "))
result = two_sum(nums, target)
print("Indices:", result)
