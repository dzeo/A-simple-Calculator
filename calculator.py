print ("This is a simple calculator app")

#for the operations
def add(num1, num2):
	return num1 + num2 

def subtract(num1, num2):
	return num1-num2

def multiplication(num1,num2):
	return num1 * num2

def division(num1, num2):
	return num1/num2

def power(num1, num2):
	return num1 ** num2

def main():
	operation = input("Select the operation you want to perform : +, -, * /, ^ \n")
			
	#To handle invalid operations
	if (operation  != "+" and operation != "-" and operation != "*" and operation  != "/" and operation != "^") :
		print ("enter a valid operation")

	#call the operations
	else:
		try:
			if operation == "+" :
				sum = add(float(input("enter the first number: ")), float(input("enter the second number: ")))
				print (sum)
			elif operation == "-" :
				sub = subtract(float(input("enter the first number: ")), float(input("enter the second number: ")))
				print (sub)
			elif operation == "*" :
				multiply = multiplication(float(input("enter the first number: ")), float(input("enter the second number: ")))
				print (multiply)
			elif operation == "/" :
				divide = division(float(input("enter the first number: ")), float(input("enter the second number: ")))
				print (divide)
			elif operation == "^" :
				pow = power(float(input("enter the first number: ")), float(input("enter the second number: ")))
				print (pow)
		except:
			print("enter a valid nuber")
i = 3
while i>0:
	main()
	i-=1
	print("you still have %d more trials" %i)
print("thats the end of the calculator segment")


