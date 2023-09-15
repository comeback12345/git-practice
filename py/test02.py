def twoSum(nums: list[int], target: int):  
    num_dict = {}  
    for i, num in enumerate(nums):  
        if target-num in num_dict.keys():  
            return [num_dict[target-num],i]  
        num_dict[num] = i
        # 如果找不到两个数的和等于目标值，返回一个空列表      
targets=26
nums= [2,7,11,15]
a=twoSum(nums=nums,target=targets)
print(a)