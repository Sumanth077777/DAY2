lower_limit = int(input("Enter the lower range: "))
upper_limit = int(input("Enter the upper range: "))
my_list = []
my_list = [x for x in range(lower_limit,upper_limit+1) if (int(x*0.5))*2==x and
sum(list(map(int,str(x))))<10]
print("The result is : ")
print(my_list)
