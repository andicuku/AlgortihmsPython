def likes(names):
	len_names = len(names)
	if len_names == 0:
		print("nobody like it")
	elif len_names == 1:
		print(f'{names[0]} likes it')
	elif len_names == 2:
		print(f"{names[0]} & {names[1]} like it")
	elif len_names == 3:
		print(f"{names[0]}, {names[1]} & {names[2]} like it")
	else:
		print(f'{names[0]}, {names[1]} & {len_names-2} other people like it')


names = ["Andi", "kevi", "besi", "klajdi"]
likes(names)
