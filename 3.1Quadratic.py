def quadratic():
    while True:

        a = int(input('input the value of а:'))
        b = int(input('input the value of b:'))
        c = int(input('input the value of c:'))
        x = int(input('input the value of x'))
        print ('The following ', "%+d" % a,end="")
        print ("x^2", end="")
        print ( "%+d" % b,end="")
        print ("x",end="")
        print ( "%+d" % c)
        print ('The value of the quadratic is ', a*x*x+b*x+c)
quadratic()