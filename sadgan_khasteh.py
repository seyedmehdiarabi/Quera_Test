a = input()
b = input()

if a == b:
    print(f"{a} = {b}")
elif int(a[::-1]) < int(b[::-1]):
    print(f"{a} < {b}")
else:
    print(f"{b} < {a}")
