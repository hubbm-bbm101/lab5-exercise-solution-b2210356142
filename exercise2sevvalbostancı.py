email = input("please enter an email")
check = [z for z in email]
x= '@'
y= '.'
if check.count(x) == 1 and check.count(y) >= 1:
    print("this is a valid email")
else:
    print("this is not a valid email")