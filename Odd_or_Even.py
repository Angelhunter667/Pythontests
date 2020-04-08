print("Setting the odds, even.")
num = input("Enter a number:")
num = int(num)
if num % 2 == 0:
    num = str(num)
    print(num + " is even.")
else:
    num = str(num)
    print(num + " is odd.")