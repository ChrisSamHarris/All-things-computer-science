def getConcatenation(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    return nums + nums 
    
print(getConcatenation([1,2,1]))
        
def removeElement(nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                # partition 
                nums[k] = nums[i]
                k += 1 
            # if we index at val, we want to skip 
        return k 
    
print(removeElement([1,2,1,4,4,4,6,7,8,9, 4, 4], 4))


list = [1,2,2,2,2,3,4,5,6,6,6,7,8,9,10]
print(set(list))

def removeDup(nums):
    """
    :type nums: List[int]
    :rtype: int
    Compare left and right, have we seen this value before? initialise pointers at L & R on index 1 
    """
    lp = 1

    for rp in range(1, len(nums)):
        if nums[rp] != nums[rp -1]:
            nums[lp] = nums[rp]
            lp += 1
    return lp
            
print(removeDup([1,2,2,2,2,3,4,5,6,6,6,7,8,9,10]))
            

