# 2.	Cho danh sách các sinh viên chứa thông tin của mỗi sinh viên [id, tên, tuổi] như sau:
students = [["SV001", "Bob", 23], [
    "SV002", "Kenny", 34], ["SV003", "Henry", 45]]
# Yêu cầu:
# a. Lấy ra thông tin của sinh viên thứ nhất và in ra định dạng "ID: {id}, name: {name} - age: {age}"
sv_1 = students[0]
sv_2 = students[1]
sv_3 = students[2]
id_1 = students[0][0]
name_1 = students[0][1]
age_1 = students[0][2]
print(f"Thông tin Sinh viên thứ 1 : {sv_1} ")
print(f"ID: {id_1} ,\tName: {name_1} , \t Age: {age_1}")

# b. Lấy ra tuổi của sinh viên thứ hai
age_1 = students[1][2]
print(f'Thông tin sinh viên 2 : {sv_2}')
print(f"tuổi của sinh viên thứ hai : {age_1}")

# c. Lấy ra thông tin hai sinh viên cuối cùng
list_sv = students[-2:]
print(f"Thông tin 2 sinh viên cuối cùng : {list_sv} ")

# d. Lấy ra id của sinh viên thứ ba
id_3 = sv_3[0]
print(f'Thông tin sinh viên 3 : {sv_3}')
print(f"ID: {id_3}")
