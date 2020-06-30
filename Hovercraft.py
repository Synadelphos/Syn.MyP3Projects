u_input = int(input())


def hovercrafts(x=u_input):
	y = 1000000
	n = x * (y * 3) - ((y * 2) * 10 + y)
	return int(n)


net = hovercrafts()


def h_outputs(x=net):
	if x > 0:
		return "Profit"
	elif x == 0:
		return "Broke Even"
	else:
		return "Loss"


final = h_outputs()


print(final)
