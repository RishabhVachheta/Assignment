def removeDuplicates(nums):
    if not nums:
        return 0
    
    # Pointer to track unique elements
    unique_ptr = 0
    
    for i in range(1, len(nums)):
        # If current element is different from the previous one
        if nums[i] != nums[unique_ptr]:
            # Move the unique element pointer ahead
            unique_ptr += 1
            # Place the unique element at its correct position
            nums[unique_ptr] = nums[i]
    
    # Returning the count of unique elements
    return unique_ptr + 1, nums[:unique_ptr + 1]

nums = [1, 1, 2]
k, modified_nums = removeDuplicates(nums)
print(f"Output: {k}, nums = {modified_nums + [None] * (len(nums) - k)}")
