a  =  [1,1,2,3,4,4,5,5,6,7,7,8,8,9,10]
b = [1,2,3]

print (list(range(1,5)))



class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_ = 1
        if len(nums)==0:
            return 0
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[len_] = nums[i]
                len_ +=1
        return len_

solutiona = Solution()
print(solutiona.removeDuplicates(b))