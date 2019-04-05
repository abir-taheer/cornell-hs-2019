x = input().split(" ")
n = int(x[0])  # number of toys
k = int(x[1])  # used per day
extra = 1 if n % k > 0 else 0
days = (n // k) + extra if n > k else 1  # number of days that it lasts

print(days)
