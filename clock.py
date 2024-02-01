a, b = map(int, input().split())
a = 12 - a
b = 60 - b
hour = a % 12
minute = b % 60
print(f"{hour:02d}:{minute:02d}")
