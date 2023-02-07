# Nhập vào một danh sách những số nguyên và hiển thị gấp đôi của các số trong danh sách sử dụng list comprehension
int_number=[int(x) for x in input("nhập vào danh sách các số nguyên : \n ").split()] # tạo ra lst dãy số với hàm split phá vỡ str đưa về int = cho x chạy hết lst bằng for
double_number = [n*2 for n in int_number] #xử lí nhân đôi lst vừa nhập
print(double_number)
