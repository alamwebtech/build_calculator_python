import math

while True:
	print("\nChoose the math operation.\n\n0 = Addition\n1 = Subtration\n3 = Multiplication\n4 = Division\n5 = Modulo\n6 Raising to a power\n7 = Square root\n8 = Sine\n9 = Cosine\n10 = Tangent\n")

oper = input("\nYour option from the menu:")

# Addition

if oper == "0":
	val1 = float(input("\nFirst value: "))
	val2 = float(input("\nSecond value: "))

	print("\nThe result is: " + str(val1+val2) + "\n")

	back = input("\nGo back to the main menu ? (y/n)")
	if back == "y":
		continue
	else:
		break

# Subtraction 

elif oper == "1":
	val1 = float(input("\nFirst value: "))
	val2 = float(input("\nSecond value: "))

	print("\nThe result is: " + str(val1-val2) + "\n")

	back = input("\nGo back to the main menu ? (y/n)")
	if back == "y":
		continue
	else:
		break

# Multiplication

elif oper == "2":
	val1 = float(input("\nFirst value: "))
	val2 = float(input("\nSecond value: "))

	print("\nThe result is: " + str(val1*val2) + "\n")

	back = input("\nGo back to the main menu ? (y/n)")
	if back == "y":
		continue
	else:
		break

# Division

elif oper == "3":
	val1 = float(input("\nFirst value: "))
	val2 = float(input("\nSecond value: "))

	print("\nThe result is: " + str(val1/val2) + "\n")

	back = input("\nGo back to the main menu ? (y/n)")
	if back == "y":
		continue
	else:
		break

# Modulo

elif oper == "4":
	val1 = float(input("\nFirst value: "))
	val2 = float(input("\nSecond value: "))

	print("\nThe result is: " + str(val1%val2) + "\n")

	back = input("\nGo back to the main menu ? (y/n)")
	if back == "y":
		continue
	else:
		break 






