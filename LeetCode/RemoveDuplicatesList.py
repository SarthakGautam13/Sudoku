#Del Function
def removeDuplicates(self, nums):
    for i in range(len(nums) - 1, -1, -1): 
        if len(nums)==1:
            return len(nums)
        if nums[i]==nums[i-1]:
            del nums[i]
    return len(nums)
#Without function ( a little confusing)
def removeDuplicates2(self, nums):
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1
    return j
