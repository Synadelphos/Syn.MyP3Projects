# get user input
u_input = int(input())


# define net profit
def hovercrafts(x=u_input):
	y = 1000000
	n = x * (y * 3) - ((y * 2) * 10 + y)
	return int(n)


# adding profit to a var
net = hovercrafts()

# determine meaning of profit
def h_outputs(x=net):
	if x > 0:
		return "Profit"
	elif x == 0:
		return "Broke Even"
	else:
		return "Loss"


# save profit to a var
final = h_outputs()

# print the output
print(final)
