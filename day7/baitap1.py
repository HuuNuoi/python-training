"""Bài tập
Cho hai tập hợp (set)
art_students = {"John", "Max", "Anna", "Bob", "Obito"}
math_students = {"Max", "Mery", "David", "Anna", "Naruto", "John"}
Tìm những người bạn học cả vẽ lẫn toán
Tìm những người bạn học vẽ nhưng không học toán
Tìm những người bạn học toán nhưng không học vẽ
Tìm những người bạn học vẽ hay toán không phải cả hai
Tìm tất cả những người bạn
"""
# Cho hai tập hợp (set)
art_students = {"John", "Max", "Anna", "Bob", "Obito"}
math_students = {"Max", "Mery", "David", "Anna", "Naruto", "John"}

# Tìm những người bạn học cả vẽ lẫn toán ( lấy phần chung dùng Giao "&")
# có thể dùng art_math_students = art_students & math_students
art_math_students = art_students.intersection(math_students)
print(f"Những người học cả vẽ lẫn toán :\n{art_math_students}")

# Tìm những người bạn học vẽ nhưng không học toán (lấy phần  "-")
art_not_math = art_students.difference(math_students)
print(f"Những người bạn học vẽ nhưng không học toán :\n{art_not_math}")

# Tìm những người bạn học vẽ hay toán không phải cả hai
not_math_art = art_students.symmetric_difference(math_students)
print(f"Những người bạn học vẽ hay toán không phải cả hai :\n{not_math_art}")

#Tìm tất cả những người bạn
all_students = art_students.union(math_students)
print(f"Tất cả những người bạn : {all_students}")
