price = float (input ("How much money did you spend? "))
if price >= 150:
    print ("Total: ", price - 50)
elif price >= 100:
    print ("Total: ", price - 25)
elif price >= 75:
    print ("Total: ", price - 15)
else:
    print ("Total: ", price)
