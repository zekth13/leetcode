class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        val = 0
        for x in range(len(nums)):
            for y in range(x+1,len(nums)):
                if nums[x]==nums[y]:
                    print(f"({x},{y})")
                    val+=1
        return val

obj = Solution()
val = obj.numIdenticalPairs([1,2,3,1,1,3])
print(val)