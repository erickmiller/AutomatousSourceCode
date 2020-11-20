"""Lab_Flatten"""
def flatten(lis):
    """Return sort flatten list"""
    ans = []
    for i in lis:
        if isinstance(i, list):
            ans = ans + flatten(i)
        else:
            ans.append(i)
    return sorted(ans)
print flatten(input())
