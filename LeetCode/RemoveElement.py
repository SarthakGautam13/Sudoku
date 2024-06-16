def removeElement(self, nums, val):
    for i in range(len(nums) - 1, -1, -1): 
        if nums[i] == val:
            del nums[i]
    return(len(nums))
removeElement(0,[0,1,2,2,3,0,4,2],2)
#The issue here is that you're modifying the list nums while iterating 
#over it using a for loop. When you remove an item from the list,
#the indices of the remaining items shift, potentially causing you to 
#skip some elements or access out-of-bounds indices. To fix this, 
#you should iterate in reverse or create a new list with
#the elements you want to keep.