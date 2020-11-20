
def print_square_root():
    y = input("Enter a number: ")
    
    y = float(y)
    
    if y <= 0:
        print("Positive numbers only, please.")
        return

    result = y**0.5
    print("The square root of", y, "is", result)

print_square_root()
