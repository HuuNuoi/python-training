# 3. Cho dict như sau: people = { "Emma": 71, "Jack": 45, "Amy": 15, "Ben" }
import json
people = {
    "Emma": 71,
    "Jack": 45,
    "Amy": 15,
    "Ben": 29
}
# In ra người già nhất
# dùng hàm max , min lấy giá trị lớn nhất trong Dict
max_age = max(people.values())
for n, a in people.items():  # dùng vòng lặp lấy từng giá trị trong dict cho đến khi gặp giá trị lớn nhất thì dừng lại
    if a == max_age:
        print(a)
        break
# cách 2 :
print(max(people, key=people.get))

# Tạo ra một dict mới dựa vào people dict với tuổi của mỗi người tăng gấp đôi
new_people = {
    name: age*2
    for name, age in people.items()
}

print(json.dumps(new_people, indent=4)) # in ra định dạng kiểu Dict định dạng chuẩn b 

# In ra enumerate các key trong people dict
# phải gán định dạng khi sử dụng hàm enumerate chỉ trả về các tuple
print(list(enumerate(people, start=1)))

# Sử dụng hàm dict để biến enumerate bên trên trở thành dict
dict_new = dict(enumerate(people,start=1))
print(json.dumps(dict_new, indent=4))