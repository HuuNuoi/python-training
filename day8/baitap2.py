# Nhập vào một năm bất kỳ. Kiểm tra xem năm đó có phải là năm nhuận hay không ?
# Năm nhuận là năm chia hết cho 4 và không chia hết cho 100 hay năm chia hết cho 400
year = int(input("Nhập vào năm :"))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(f"năm {year} là năm nhuận")
else:
    print(f"năm {year} không phải là năm nhuận")
