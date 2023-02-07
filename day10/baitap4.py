number = [100, 34, 44, 67, 89, 11, 27, 9, 16, 77]
new_number = [x for x in number if x % 2 != 0]
print(new_number)
print(sum(new_number))
new1 = [v*2 if v % 2 == 0 else v*3 for v in number]
print(new1)

# 4. Sử dụng zip function để tạo 2 lists sau trở thành một dict
fruits  = ["banana", "apple", "kiwi", "mango", "cherry", "orange"]
amounts = [ 12,       34,      90,     100,     300,      45,    60, 70, 678]
import json

fruits_info = dict(zip(fruits, amounts))
print(json.dumps(fruits_info, indent=4))
