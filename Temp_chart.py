def Temperature():
   F = int(input("Enter temperature in Farenhiet: "))
   C = ((5.0 / 9.0) * (F - 32))
   print("Temperature in degreee Celsius is ", C)
   print("Temperature you in celsius was ", F)


a="yes"
while a=="yes":
   Temperature()
   a=input("would you like to continue?")


celsius = 0
while celsius <= 100:
   fahrenheit=(celsius + 32)
   print(celsius, "     ", fahrenheit)
   celsius+=5