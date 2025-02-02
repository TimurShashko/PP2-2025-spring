def neigh_3_n_3(nums):
    for i in range (0,len(nums)):
        if nums[i]==3:
            if (i<=len(nums)-2):
                if (nums[i]==nums[i+1]):
                    return True
    return False

nums=[1, 3, 3]
print(neigh_3_n_3(nums))
nums=[1, 3, 1, 3]
print(neigh_3_n_3(nums))
print("")