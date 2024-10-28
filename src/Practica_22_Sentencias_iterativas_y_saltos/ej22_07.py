
def tablas():
    for i in range (1, 11):
        for n in range (0, 11):
            print(f"{i} * {n} = {i*n}")
        print("------------")


def main():
    tablas()


if __name__ == "__main__":
    main()