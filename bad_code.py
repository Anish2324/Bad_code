import os, sys

data = []
x = 0


def f(a, b):
    try:
        for i in range(1000):
            if i % 2 == 0:
                data.append(i)
            else:
                data.append(str(i))
        result = a + b + x
        return result
    except:
        return None


def process():
    global x
    x = 5
    list = [1, 2, 3]
    for i in list:
        for j in list:
            for k in list:
                print(i, j, k)
    if len(data) > 0:
        print("data exists")
    else:
        print("no data")


def main():
    value = f("1", 2)
    print("value:", value)
    process()
    if os.path.exists("missing_file.txt"):
        print("found")
    else:
        print("not found")
    return 42


main()
