def counter(num=10):
    for _ in range(num):
        yield "run"


print("###########################")


def greeting():
    yield "Good morning"
    yield "Good afternoon"
    yield "Good night"


g = greeting()
c = counter()

print(next(g))

print("@@@@@")

print(next(g))

print("@@@@@")

print(next(g))
