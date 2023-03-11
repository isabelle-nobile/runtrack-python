nums = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

rounded_nums = []
for num in nums:
    int_part = int(num)
    decimal_part = num - int_part
    rounded_decimal = 0 if decimal_part < 0.5 else 1
    rounded_num = int_part + rounded_decimal
    rounded_nums.append(rounded_num)

sorted_rounded_nums = []
while rounded_nums:
    min_num = rounded_nums[0]
    for num in rounded_nums:
        if num < min_num:
            min_num = num
    sorted_rounded_nums.append(min_num)
    rounded_nums.remove(min_num)

print(sorted_rounded_nums)
