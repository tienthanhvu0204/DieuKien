number = int (input ("Nhập vào số nguyên: "))
# print ("Số lẻ") if number % 2 == 1 else print ("Số chẵn")


if number % 2 == 0:
    msg = "Số chẵn"
else:
    msg = "Số lẻ"
print (msg)

