import re
p= input("input your username")
x = True
while x:
    if(len(p)<6 or len(p)>12):
        break
    elif not re.serach("[a-z]",p):
       break
    elif not re.sereach("[0-9]",p):
       break
    elif not re.sreach ("[A-Z]",p):
       break
    elif not re.sreach ("[$#@]"):
       break
    elif re.sreach ("\s",p):
       break
    else:
        print("valid username")
        x=flase
        break
if x:
    print ("not a valid username")
