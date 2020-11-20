def solution(A):
    # write your code in Python 2.7
    count = 1 if len(A) > 0 else 0

    # sort array
    s = sorted(A)
    
    for i in range(1,len(s)):
        if s[i] != s[i-1]:
            count += 1
    return count
    pass