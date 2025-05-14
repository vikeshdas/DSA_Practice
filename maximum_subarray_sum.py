"""
-every time compare cur_sum with max_sum and if cur_sum is greater then max_sum then update max_sum with cur_sum
- when current_sum become negetive reset it with zero.

"""

def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_sum=float('-inf')
    cur_sum=0
    for num in nums:
        cur_sum+=num
        max_sum=max(max_sum,cur_sum)
        if cur_sum<0:
            cur_sum=0
    return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))