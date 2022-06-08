from blog.package_1.package_a import PackageA
from blog.package_1.package_a import test_a
from blog.package_2.package_b import PackageB
from blog.package_2.package_b import test_b



def main():
    print("I'm a command!")
    name = input('Please type your name')
    print(f"Hi {name}")

    pack1 = PackageA("Test", "for", "A")
    print(pack1.a1, pack1.a2, pack1.a3)
    test_a()

    pack2 = PackageB("Test", "for", "B")
    print(pack2.b1, pack2.b2, pack2.b3)
    test_b()

    for lol in range(11):
        print("It's okay to interrupt a Zoom recording for 2 seconds!")


if __name__ == '__main__':
    main()
