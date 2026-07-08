class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]: 
        seen=set()
        answer=[]
        for num in nums:
            seen.add(num)
        for i in range(1, len(nums)+1):
            if i not in seen:
                answer.append(i)

        return answer
        