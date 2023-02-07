'''
2. Tạo một set trống có tên là set_a
a. Thêm 'Anna' vào set_a
b. Thêm một tuple ('Kenny', 'Jen', 'Danny')
c. In ra set_a và tính chiều dài của nó
d. Xóa 'Jen' ra khỏi set_a
e. Xóa tất cả các giá trị từ set_a
'''

set_a = set()
#a
set_a.add ("Anna") 
#b
tuple_1 = ('Kenny','Jen','Danny')
set_a.update(tuple_1)

#c
print(f"In set a : {set_a}") #set là cấu trúc dữ liệu không theo thứ tự nhất định , không trùng lặp, không thể truy cập bằng chỉ số
print(f"Độ dài của set_a : {len(set_a)}")

#d
set_a.remove("Jen")
print(set_a)

#e
set()


