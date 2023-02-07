# 1. Đếm số chẵn và lẻ trong đoạn [0, 1000] theo 2 cách: thông thường và list comprehension
# Cách 1: thông thường
odd = even = 0

for n in range(0, 1001):
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print(f"Số lượng giá trị chẵn trong [0, 1000]\t: {even}")
print(f"Số lượng giá trị lẻ trong [0, 1000]\t: {odd}")
# cách 2
odd = sum([1 for n in range(1001) if n % 2 != 0])
even = sum([1 for n in range(1001) if n % 2 == 0])
print(f"Số lượng giá trị chẵn trong [0, 1000]\t: {even}")
print(f"Số lượng giá trị lẻ trong [0, 1000]\t: {odd}")
