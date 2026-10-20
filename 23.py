try:
    n = int(input("Number: "))
    print(10/n)
except ValuError:
    print("Please enter avalid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Done")

