def parcourir_nombres(start_range, end_range, nums):
    result = [i for i in range(start_range,end_range) if i not in nums]
    return result

start_range = 0
end_range = 101
nums = [26, 37, 88]
print(parcourir_nombres(start_range,end_range,nums))
