# Định nghĩa 4 hàm add, subtract, divide, multiply (+, -, /, *). Mỗi hàm nhận vào hai tham số thực hiện lần lượt các phép toán cộng, trừ, chia, nhân. Lưu ý hàm nên trả về thay vì in ra.
def add(num1, num2):
    return num1 + num2

def divine(num1, num2):
    return 'Divide by zero' if num2==0 else num1 / num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

number1 = int(input("input number 1: "))
number2 = int(input("input number 2: "))

total = add(number1, number2)
print(total)
    
sub=subtract(number1, number2)
print(sub)

mul=multiply(number1, number2)
print(mul)

div=divine(number1, number2)
print(div)