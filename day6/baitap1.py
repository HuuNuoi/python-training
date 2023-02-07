'''
1. Cho một list chứa các tuple như sau: friends = [("Bob", "Male"), ("Anna", "Female"), ("Max", "Male")]
a. Cho biết chiều dài của friends
b. Lấy ra phần tử đầu, cuối và giữa và kiểm tra kiểu của chúng
c. Nhập vào tên (name) và giới tính (gender) của một người bạn sau đó append vào friends tuple gồm hai giá trị (name, gender)
2. Tạo một set trống có tên là set_a
a. Thêm 'Anna' vào set_a
b. Thêm một tuple ('Kenny', 'Jen', 'Danny')
c. In ra set_a và tính chiều dài của nó
d. Xóa 'Jen' ra khỏi set_a
e. Xóa tất cả các giá trị từ set_a
'''
# 1. Cho một list chứa các tuple như sau: friends = [("Bob", "Male"), ("Anna", "Female"), ("Max", "Male")]
# a. Cho biết chiều dài của friends
friends = [("Bob", "Male"),
           ("Anna", "Female"),
           ("Max", "Male")]
friends_a = len(friends)
print(f"Chiều dài của friends : {friends_a}")

# b. Lấy ra phần tử đầu, cuối và giữa và kiểm tra kiểu của chúng
friends_1 = friends[0]
friends_2 = friends[1]
friends_3 = friends[-1]
print(type(friends_1))
print(type(friends_2))
print(type(friends_3))

# c. Nhập vào tên (name) và giới tính (gender) của một người bạn sau đó append vào friends tuple gồm hai giá trị (name, gender)
friend_n = input("nhập tên của người bạn : ")
friend_g = input("Giới tính : ")
friends_new = (friend_n, friend_g)
# Tuple không thể thay đổi thuộc tính bên trong nên dungaf append bị lỗi , thay thế bằng toán tử
friends.append(friends_new)
print(f"Danh sách sau khi append : {friends}")
