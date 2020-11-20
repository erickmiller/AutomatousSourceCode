def to_digits(n):
    digits = []

    while n != 0:
        digits = [n % 10] + digits
        n //= 10
        
    return digits

def to_number(n):
    number = 0

    for digit in n:
        number = number * 10 + digit

    return number
    
def max_number(n):
    return to_number(sorted(to_digits(n), reverse=True))

def min_number(n):
    return to_number(sorted(to_digits(n)))

def sort_n(n, m):
    flag = True
    if m == 0:
        flag = False
    return to_number(sorted(to_digits(n), reverse=flag))

if __name__ == "__main__":
    n = input("Enter n: ")
    n = int(n)

    print("Largest:", sort_n(n, 1))
    print("Smallest:", sort_n(n, 0))
        

    
