def fibonacci(num: int) -> int:

    a = 0
    b = 1

    for i in range(num):

        a = a + b
        b =  a

        return b

