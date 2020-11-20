def newton_update(f, df):
    def update(x):
        return x - f(x) / df(x)
    return update

def find_zero(f, df):
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero)


def square_root_newton(a):
    # 计算(一次, 普通?)平方根的程序
    def f(x):
        return x * x - a
    def df(x):
        return 2 * x
    return find_zero(f, df)

# >>> square_root_newton(64)
# 8.0
