import math


aB = int(input())
bC = int(input())
# print(str(int(round(math.degrees(math.atan2(aB, bC))))) + chr(176))
print(f'{str(int(round(math.degrees(math.atan2(aB, bC)))))}\xb0')
