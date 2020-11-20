import math
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/api')
def index():
    q = request.args.get('q')
    try:
        result = str(api(request.args))
        print q, '=>', result
        return result
    except Exception, e:
        return str(0)

@app.route('/api2')
def index2():
    q = request.args.get('q')
    result = str(api(request.args))
    print q, '=>', result
    return result

def api(args):
    q = args['q']
    if "largest" in q or "primes" in q:
        hash = q.split(':')[0]
        text = q.split(':')[1]
        numbers = q.split(':')[2]
        numbers = map(int, numbers.split(', '))
        if "largest" in q:
            return largest(numbers)
        else:
            return ','.join(map(str, prime(numbers)))
    elif "anagram" in q:
        hash = q.split(':')[0]
        text = q.split(':')[1]
        text2 = q.split(':')[2]
        text = text.split(' ')
        text2 = text2.split(' ')
        check = text[9][1:-1]
        words = [x.replace(',', '') for x in text2[1:]]
        anagrams = filter(lambda x: is_anagram(check, x), words)
        return ','.join(anagrams)
    elif "plus" in q or "multiplied" in q or 'minus' in q:
        # 14 plus 19 multiplied by 19
        hash = q.split(':')[0]
        text = q.split(':')[1]
        text = text.replace(" what is ", '')
        text = text.replace("plus", '+')
        text = text.replace("multiplied by", '*')
        text = text.replace("multiplied", '*')
        text = text.replace("minus", '-')
        return eval(text)
    elif "plus" in q and "multiplied" in q:
        hash = q.split(':')[0]
        text = q.split(':')[1]
        text = text.split(' ')
        x = int(text[3])
        y = int(text[5])
        z = int(text[8])
        return x + (y*z)
    elif "plus" in q or "multiplied" in q or "minus" in q:
        hash = q.split(':')[0]
        text = q.split(':')[1]
        text = text.split(' ')
        x = int(text[3])
        y = int(text[5])
        if "plus" in q:
            return plus([x, y])
        elif "multiplied" in q:
            return x * y
        else:
            return x - y
    elif "Fibonacci" in q:
        hash = q.split(':')[0]
        text = q.split(':')[1]
        index = text.split(' ')[4][:-2]
        return fibo(int(index))
    elif "square and a cube" in q:
        hash = q.split(':')[0]
        text = q.split(':')[1]
        number_str = q.split(':')[2]
        numbers = map(int, number_str.split(','))
        return ','.join(map(str, square_and_cube(numbers)))
    elif "capital" in q and "USA" in q:
        return "Washington, D.C."
    elif "Eiffel tower in" in q:
        return "Paris"
    elif "James Bond" in q:
        return "Sean Connery"
    elif "currency" in q and "Spain":
        return "peseta"
    elif "power of" in q:
        hash = q.split(':')[0]
        text = q.split(':')[1]
        text = text.split(' ')
        x = int(text[3])
        y = int(text[8])
        return x ** y
    return -1

def largest(numbers):
    return max(numbers)

def plus(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

def square_and_cube(numbers):
    return filter(is_square_and_cube, numbers)

def is_square_and_cube(number):
    square_root = number ** 0.5
    cube_root = number ** (1/3.0)
    return equal_float(square_root, int(square_root)) and equal_float(cube_root, int(cube_root))

def equal_float(a, b):
    return abs(a - b) < 0.00001

def prime(numbers):
    return filter(is_prime, numbers)

def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def fibo(n):
    if n < 2:
        return n
    return fibo(n-2) + fibo(n-1)

def is_anagram(a, b):
    return sorted(list(a)) == sorted(list(b))

if __name__ == '__main__':
    app.run(debug=True)
