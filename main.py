import hello # I think we prefer this
from hello import world # instead this

def myfunc():
    d = {"some key": "value", "other key": 7}
    return d

def main():
    print("SUCCESS")
    print(world.get_random_number_multiplied(5))
    print(hello.world.get_random_number_multiplied())
    print("Your dictionary:", myfunc())
    print("Function signature", myfunc)

    for i in range(3):
        print("#")

if __name__ == "__main__":
    main()

