import time
from fractions import gcd
import math

start_time = time.time()


# def is_int_dist(a, b, c):
#     square = min(
#         a ** 2 + (b + c) ** 2,
#         b ** 2 + (a + c) ** 2,
#         c ** 2 + (b + a) ** 2
#     )
#     root = math.sqrt(square)
#     return root % 1 == 0

#
#
# def is_int_dist_2(a, b, c):
#     square = c ** 2 + (b + a) ** 2
#     root = math.sqrt(square)
#     return root % 1
#
# squares = {}
#
#
# assert is_int_dist(3, 5, 6)

LIMIT = 99
pyt = {}

for m in xrange(1, LIMIT):
    for n in xrange(m + 1, LIMIT):
        k = 1
        a = n ** 2 - m ** 2
        b = 2 * m * n
        if (m - n) % 2 == 0 or gcd(m, n) != 1:
            continue

        while True:
            temp_a = a * k
            temp_b = b * k
            max_pyt = max(temp_a, temp_b)
            min_pyt = min(temp_a, temp_b)
            if min_pyt > LIMIT:
                break
            pyt[min_pyt, max_pyt] = 1
            k += 1

counter = 0
print pyt
for a, b in pyt:
    temp = b // 2

    if temp >= LIMIT:
        continue
    elif b < LIMIT:
        counter += (a // 2)

    if temp <= a:
        counter += (a - temp)
        if (a - temp) % 2 == 0:
            counter += 1

    print a, b, counter


# for i in range(1, LIMIT):
#     for j in range(i, LIMIT):
#         for k in range(j, LIMIT):
#             if is_int_dist(i, j, k):
#                 counter += 1

print counter

print time.time() - start_time, "seconds"
