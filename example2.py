coffee = 5
while 1:
	print("Please enter coin")
	coin = 0
	coin = int(input())
	if not coffee:
		print("Sold Out")
		break
	elif coin<300:
		print("Coin is more required")
	elif coin == 300:
		print("I give you coffee")
		coffee = coffee -1
	else:
		coffee = coffee -1
		change = 0
		change = coin-300
		print("I give you coffee and change %d" %change)

	
