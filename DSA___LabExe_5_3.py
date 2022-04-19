#Problem 3:
#Create a program that will give an output as shown on figure A.
#The program will ask to input three customers information.
#Each customer have three items purchased. Used the given structure below.

def name():
	firstName = input("First Name: ")
	lastName = input("Last Name: ")
	return lastName, firstName

def item():
	itemCode = input("ID: ")
	itemName = input("Name: ")
	itemPrice = input("Price: ")
	itemPrice = itemPrice + ".00"
	return itemCode, itemName, itemPrice

def order():
	print("Order Date:")
	day = input("Day: ")
	month = input("Month: ")
	year = input("Year: ")
	date = month + "/" + day + "/" + year

	print("Enter 3 items")
	code1, name1, price1 = item()
	quantity1 = input("Quantity: ")
	code2, name2, price2 = item()
	quantity2 = input("Quantity: ")
	code3, name3, price3 = item()
	quantity3 = input("Quantity: ")
	return date, code1, name1, price1, quantity1, code2, name2, price2, quantity2, code3, name3, price3, quantity3

print("Enter 3 Customers")

class customer1():
	print("\nCUSTOMER INFORMATION 1")
	lastName, firstName = name()
	contactNo = input("Contact No: ")
	date, code1, name1, price1, quantity1, code2, name2, price2, quantity2, code3, name3, price3, quantity3 = order()
	totalPrice = float(price1)*float(quantity1) + float(price2)*float(quantity2) + float(price3)*float(quantity3)

class customer2():
	print("\nCUSTOMER INFORMATION 2")
	lastName, firstName = name()
	contactNo = input("Contact No: ")
	date, code1, name1, price1, quantity1, code2, name2, price2, quantity2, code3, name3, price3, quantity3 = order()
	totalPrice = float(price1)*float(quantity1) + float(price2)*float(quantity2) + float(price3)*float(quantity3)

class customer3():
	print("\nCUSTOMER INFORMATION 3")
	lastName, firstName = name()
	contactNo = input("Contact No: ")
	date, code1, name1, price1, quantity1, code2, name2, price2, quantity2, code3, name3, price3, quantity3 = order()
	totalPrice = float(price1)*float(quantity1) + float(price2)*float(quantity2) + float(price3)*float(quantity3)
	
print("\nSUMMARY REPORT")

print("{:>3} {:>25} {:>12} {:>13} {:>7} {:>9}".format("#", "Customer Name", "Order Date", "Items", "Price", "Quantity"))
print("{:>3} {:>25} {:>12}".format("1", customer1.lastName + ", " + customer1.firstName, customer1.date))
print("{:>56} {:>7} {:>9}".format(customer1.name1, customer1.price1, customer1.quantity1))
print("{:>56} {:>7} {:>9}".format(customer1.name2, customer1.price2, customer1.quantity2))
print("{:>56} {:>7} {:>9}".format(customer1.name3, customer1.price3, customer1.quantity3))
print("{:>56} {:>17}".format("TOTAL PRICE: ", str(customer1.totalPrice) + "0"))

print("{:>3} {:>25} {:>12}".format("2", customer2.lastName + ", " + customer2.firstName, customer2.date))
print("{:>56} {:>7} {:>9}".format(customer2.name1, customer2.price1, customer2.quantity1))
print("{:>56} {:>7} {:>9}".format(customer2.name2, customer2.price2, customer2.quantity2))
print("{:>56} {:>7} {:>9}".format(customer2.name3, customer2.price3, customer2.quantity3))
print("{:>56} {:>17}".format("TOTAL PRICE: ", str(customer2.totalPrice) + "0"))

print("{:>3} {:>25} {:>12}".format("3", customer3.lastName + ", " + customer3.firstName, customer3.date))
print("{:>56} {:>7} {:>9}".format(customer3.name1, customer3.price1, customer3.quantity1))
print("{:>56} {:>7} {:>9}".format(customer3.name2, customer3.price2, customer3.quantity2))
print("{:>56} {:>7} {:>9}".format(customer3.name3, customer3.price3, customer3.quantity3))
print("{:>56} {:>17}".format("TOTAL PRICE: ", str(customer3.totalPrice) + "0"))