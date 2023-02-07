friends = ["Jen", "Jack", "Kenny", "Jelly",
           "Bob", "Henry", "Anne"]
#   1
# a. Lấy ra 4 người bạn đầu tiên trong friends
friends_a = friends[0:4]
print(f"Lấy ra 4 người bạn đầu tiên trong friends : \n{friends_a}")
#   b. Lấy ra 4 người bạn cuối trong friends
friends_b = friends[-4:]
print(f"Lấy ra 4 người bạn cuối trong friends : \n{friends_b}")
#   c. Đảo ngược danh sách friends
friends_c = friends[::-1]
print(f"Đảo ngược danh sách friends : \n{friends_c}")
#   d. Lấy ra những người bạn từ vị trí 1 đến hết
friends_d = friends[1::]
print(f"Lấy ra những người bạn từ vị trí 1 đến hết : \n{friends_d}")
# •	e. Copy danh sách ban đầu thành một danh sách mới
friends_e = friends[:]
print(f" Copy danh sách ban đầu thành một danh sách mới : \n{friends_e}")
#   f. Lấy ra những người bạn từ vị trí 2 đến sát cuối
friends_f = friends[1:-1]
print(f"Lấy ra những người bạn từ vị trí 2 đến sát cuối : \n{friends_f}")


# 2.	Cho danh sách các sinh viên chứa thông tin của mỗi sinh viên [id, tên, tuổi] như sau:
# students = [["SV001", "Bob", 23], ["SV002", "Kenny", 34], ["SV003", "Henry", 45]]
# Yêu cầu:
# a. Lấy ra thông tin của sinh viên thứ nhất và in ra định dạng "ID: {id}, name: {name} - age: {age}"
# b. Lấy ra tuổi của sinh viên thứ hai
# c. Lấy ra thông tin hai sinh viên cuối cùng
# d. Lấy ra id của sinh viên thứ ba
