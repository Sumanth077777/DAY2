def reverse(s):
    str=" "
    for i in s:
        str=i+str
        return str
s="rajasekharreddy"
print("The original string is :", end=" ")
print(s)
print("The reverse string (using loops):" ,end=" ")
print(reverse(s))
