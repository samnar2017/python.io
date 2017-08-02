
def greeting():
    while True:
            a=str(input("what is your name?:"))
            print ('Nice to meet you ',a)
            b=str(input("what is your favorite color?:"))
            print (b, 'that is a nice color')
            answer=str(input("Wanna go again?"))
            print (answer)
            if answer == 'no':
                          break
greeting()