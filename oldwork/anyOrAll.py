numCount = int(input())
nums = input().split()
testCases = all(int(element) >= 0 for element in nums) and any(num == num[::-1] for num in nums)
print(testCases)
