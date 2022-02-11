def PowerOfTwo(Power):

    i = 1
    res = 1

    while i <= Power:
        res = res * 2
        i = i + 1
    print(res)

PowerOfTwo(int(input("Enter power of 2: ")))