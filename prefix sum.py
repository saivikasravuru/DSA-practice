def prefix_sum_array(nums):
    prefix = [0] * len(nums)
    prefix[0] = nums[0]
    for i in range(1, len(nums)):
        prefix[i] = prefix[i - 1] + nums[i]
    return prefix

# 🔽 Take input from the user
nums = list(map(int, input("Enter numbers separated by space: ").split()))
prefix = prefix_sum_array(nums)
print("Prefix Sum Array:", prefix)

try:
    # 🔄 Ask for range query
    l = int(input("Enter start index of range (0-based): "))
    r = int(input("Enter end index of range (0-based): "))

    # Validate range
    if l < 0 or r >= len(nums) or l > r:
        print("❌ Invalid range. Make sure 0 ≤ l ≤ r < len(nums).")
    else:
        range_sum = prefix[r] - (prefix[l - 1] if l > 0 else 0)
        print(f"✅ Sum from index {l} to {r}: {range_sum}")

except ValueError:
    print("❌ Please enter only integer values for indices.")
