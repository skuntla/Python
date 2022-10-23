'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

nums = [-1,-2,-3,-4,-5]
target = -8
#output shuold be [0,4]

# for i in range(len(nums)):
#     if nums[i] > target:
#         pass
#     else:
#         for j in range(i+1,len(nums)):
#             if target == nums[i] + nums[j]:
#                 print(i,j, nums[i], nums[j])
                # return f"found {i}, {j}"
                

# Above method is O(n^2)



temp_dict={}
for i in range(len(nums)):
    diff = target - nums[i]
    
    if diff in temp_dict:
        print([temp_dict[diff],i])
    temp_dict[nums[i]] = i
    
        # return [temp_dict[diff],i]

