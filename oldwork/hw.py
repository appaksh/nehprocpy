inp = input()
result = [str(2 * int(c)) for c in inp if c.isdigit()]
print("".join(result))

