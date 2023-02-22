from art import logo

def add(n1, n2):
	return n1 + n2

def sub(n1, n2):
	return n1 - n2

def multi(n1, n2):
	return n1 * n2

def divide(n1, n2):
	return n1 / n2

operations = {
 "+":add,
 "-":sub,
 "*":multi,
 "/":divide
}

def calculate():
	print(logo)
	num1 = float(input("What is the first number: "))

	for symbols in operations:
		print(symbols)
	should_continue = True

	while should_continue:
		operation_symbols = input("Pick the opertation: ")
		num2 = float(input("What is the second number: "))
		calculation_function = operations[operation_symbols]
		answer = calculation_function(num1, num2)

		print(f"{num1} {operation_symbols} {num2} = {answer}")

		if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
			num1 = answer
		else:
			should_continue = False
			calculate()

calculate()