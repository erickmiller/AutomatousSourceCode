user_input = float(input("Please enter a positive number...\n"))

def square_root(x):
     count = 0
     ballpark_num = 1
     while round(ballpark_num**2 - user_input,2) != 0:
         new_number = 0.5*(ballpark_num + (x/ballpark_num))
         ballpark_num = new_number
         count += 1
         print("Count is {} number is {}".format(count,ballpark_num))
     return new_number
print("The Square Root of {} is {}".format(user_input, square_root(user_input)))
