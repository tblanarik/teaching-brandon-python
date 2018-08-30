import hello # I think we prefer this
from hello import world # instead of this
import itertools

def myfunc():
    d = {"some key": "value", "other key": 7}
    return d

def myfunc2():
    return "A", 3.1415

def main():
    # Print something
    print("SUCCESS")

    # Call the function from the imported module
    print(world.get_random_number_multiplied(5))

    # Call the function using the package.module name
    print(hello.world.get_random_number_multiplied())

    # Print the dictionary that returns from myfunc
    print("Your dictionary:", myfunc())

    # Print myfunc the function signature
    print("Function signature", myfunc)

    # Print the tuple return value from myfunc2
    print(myfunc2())

    # Basic for-loop
    for i in range(3):
        print("#")

    # Itertools combinations!
    print(list(itertools.combinations([1,2,3, 4], 3)))

if __name__ == "__main__":
    main()

