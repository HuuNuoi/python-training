# Nhập hai số a và b từ bàn phím. In ra số lớn nhất và nhỏ nhất trong hai số
""" a = float(input("nhập số a : "))
b = float(input("nhập số b : "))
if a > b:
    print(f"số lớn nhất là : {a}")
    print(f"số nhỏ nhất là : {b}")
elif a == b:
    print(f" hai số bằng nhau {a} = {b}")
    
else :
    print(f"số lớn nhất là  : {b}")
    print(f"số nhỏ nhất là : {a}")
 """
# C2
a, b = map(float, input("nhập a và b : ").split())
print(a, b, sep=" và ")
if a > b:
    print(f"số lớn nhất là {a}")
    printf(f"số nhỏ nhất là {b}")
else:
    print(f"số lớn nhất là {b}")
    print(f"số nhỏ nhất là {a}")
