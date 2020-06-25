# For the values 1 through 100 create a script that prints 1 through 100 and replaces numbers divisible by 3 with
# Fizz!, divisible by 5 with Buzz! and divisible by both 3 and 5 with Fizz!Buzz!

# Step one: create a sufficient range of the numbers 1-100
for i in range(1, 101):
	# numbers divisible by both
	if i % 3 == 0.0 and i % 5 == 0.0:
		print("Fizz!Buzz!")
	# divisible by 3
	elif i % 3 == 0.0:
		print("Fizz!")
	# divisible by 5
	elif i % 5 == 0.0:
		print("Buzz!")
	# divisible by neither
	elif i % 3 != 0.0 and i % 5 != 0.0:
		print(i)