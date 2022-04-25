ChieuCao = float (input ("Bạn cao bao nhiêu? (m) "))
CanNang = float (input ("Bạn nặng bao nhiêu kg? "))
BMI = CanNang / (ChieuCao * ChieuCao)
if BMI < 16:
    msg = "gầy cấp độ III"
elif BMI < 17:
    msg = "gầy cấp độ II"
elif BMI < 18.5:
    msg = "gầy cấp độ I"
elif BMI < 25:
    msg = "bình thường"
elif BMI < 30:
    msg = "thừa cân"
elif BMI < 35:
    msg = "béo phì cấp độ I"
elif BMI < 40:
    msg = "béo phì cấp độ II"
else:
    msg = "béo phì cấp độ III"
print ("Tình trạng của bạn là ", msg)



