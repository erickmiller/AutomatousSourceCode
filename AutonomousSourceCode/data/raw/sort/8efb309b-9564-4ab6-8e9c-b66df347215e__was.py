from operator import itemgetter, attrgetter, methodcaller


def sort_by_end(l):
    return sorted(l, key=itemgetter(1))


def pred(sorted_jobs, j):
    begin_time = sorted_jobs[j-1][0]
    i = j-1
    while sorted_jobs[i][1] > begin_time:
        if i < 0:
            break
        i -= 1

    if i < 0:
        return 0

    return i+1

def was(sorted_jobs):
    dp = [0 for _ in range(0,n_jobs+1)]

    for i in range(1, n_jobs+1):
        dp[i] = max(sorted_jobs[i-1][2] + dp[pred(sorted_jobs, i)], dp[i-1])

    return dp[n_jobs]


if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        n_jobs = int(input())

        jobs = []

        for _ in range(n_jobs):
            inp = list(map(int, input().split()))

            jobs.append([inp[0], inp[1], inp[2]])

        # Sort according to 'end'
        sorted_jobs = sort_by_end(jobs)

        res = was(sorted_jobs)

        print(res)