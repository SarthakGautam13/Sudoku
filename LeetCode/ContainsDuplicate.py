#Brute Force
def containsDuplicate(self, nums):
    for i in range(0,len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j]:
                return True
    return False
containsDuplicate(0,[2,14,18,22,22])
# Sort method 
def containsDuplicate2(self, nums):
    nums.sort()
    a = len(nums)
    for i in range(1,len(a)):
        if nums[i]==nums[i-1]:
            return True
    return False