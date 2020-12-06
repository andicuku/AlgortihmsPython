#finding greatest common divisior between two numbers a and b

a = int(input("Enter first number "))
b = int(input("enter second number "))
#checking if numbers are different
while a!=b:
	#if a gretaer than b then a is equal to a minus b
	if a>b:
		a=a-b
	else:
		b=b-a
#printing output
print(a)

