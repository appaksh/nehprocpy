def fibonacci(n):
    fibList = [0, 1]
    for rep in range(2, n):
        fibList.append(fibList[-1] + fibList[-2])

    return fibList[:n]



if __name__ == '__main__':
    n = int(input())
    print(list(map(lambda x: x ** 3, fibonacci(n))))
