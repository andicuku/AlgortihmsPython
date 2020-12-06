def decimal_binary(number):
	string = ""
	while number > 0:
		reminder = number%2
		if reminder==1:
			string = str(1)+string
		else:
			string=string+str(0)
		number=(number-reminder)/2
	return string



number = int(input())
print(decimal_binary(number))