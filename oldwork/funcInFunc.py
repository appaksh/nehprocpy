def outerFunc(func):
    def innerFunc():
        print("Hi")
        func()

    return innerFunc


def func2():
    print("Bye")


func2()
