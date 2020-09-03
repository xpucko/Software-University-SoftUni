x = "global"


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    def change_local():
        global x
        x = "global: changed!"

    print("outer:", x)
    inner()
    print("outer:", x)
    change_local()


print(x)
outer()
print(x)
