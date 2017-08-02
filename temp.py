def Temperature():
    temp = int(input("Please enter a temperature in Farenheit: "))
    print ("Farenheit",temp, "    Celsius", ((temp-30)/2))

a="yes"
while a=="yes":
   Temperature()
   a=input("would you like to continue?")


