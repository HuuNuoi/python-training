# Nhập vào một số nguyên n. Kiểm tra và in ra n là số chẵn hay lẻ
integer = int(input("Input integer : "))
s = "it's even"
if integer % 2 != 0:
    s = "It's odd"
    print(s)
