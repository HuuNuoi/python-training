# Giải và biện luận phương trình bậc nhất một hai ax^2 + bx + c = 0 (ẩn x, a, b, c là ba số cho trước)
a, b, c = map(eval, input("nhập giá trị a, b, c : ").split())
print(f"Phương trình bậc nhất một hai có biểu thức :  {a}x^2 + {b}x + {c} = 0")
if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        print(f"Phương trình có nghiệm duy nhất x = {-c/b}")
else:
    denta = b**2 - 4*a*c
    if denta > 0:
        x1 = (-b + denta**0.5) / (2*a)
        x2 = (-b - denta**0.5) / (2*a)
        print(f"Phương trình có 2 nghiệm phân biệt : x1 = {x1} & x2 = {x2}")
    elif denta == 0:
        print(f" Phương Trình có nghiệm kép x1 = x2 = {-b/(2*a)}")
    else:
        print("Phương trình vô nghiệm")
