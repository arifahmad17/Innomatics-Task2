#Find Numbers with Even Number of Digits

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even=0
        for i in range(0,len(nums)):
            l=len(str(nums[i]))
            if l%2==0:
                even=even+1
        return even
            
