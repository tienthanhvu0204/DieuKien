a = input ("Nhập số: ")
number = float (a)
if number % 2 == 0:
    msg = "Số chẵn"
elif number % 2 == 1:
    msg = "Số lẻ"
else:
    msg = "Số nhập không phải số tự nhiên"
print (msg)