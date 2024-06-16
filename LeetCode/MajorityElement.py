#Moore Voting Algorithm 
def majorityElement(self, nums):
    count=0
    candidate=0 
    for i in nums:
        if count==0:
            candidate=i
        if i == candidate:
            count+=1
        else:
            count-=1
    return candidate
# Since character always greater or equal to len//2
def majorityElement2(self,nums):
    nums.sort()
    return nums[len(nums)//2]
majorityElement2(0,[1,2,2,2,1,3]) 