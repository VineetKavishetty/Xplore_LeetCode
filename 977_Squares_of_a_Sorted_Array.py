class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sq=[]
        for num in nums:
            sq.append(num**2)
        sq.sort()
        return sq
