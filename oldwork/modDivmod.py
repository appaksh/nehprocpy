num = int(input())
mod = int(input())
divMod = divmod(num, mod)
print(*divMod, divMod, sep='\n')
