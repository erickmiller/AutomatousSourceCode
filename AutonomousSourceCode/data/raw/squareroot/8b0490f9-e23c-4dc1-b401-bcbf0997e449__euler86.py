def is_square(n):
    root = int(n**0.5)
    return root * root == n

def euler86():
    size = 0
    M = 1
    target = 1000000

    while True:
        for ab in range(2, 2*M+1):
                if is_square((ab)**2 + M**2):
                    if ab < M: size += ab/2
                    else: size += (ab/2-(ab-M)+1)
                    if size > target: return M
        M += 1

if __name__ == "__main__":
    print euler86()
