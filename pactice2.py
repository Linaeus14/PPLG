def main():
    print("""
    *****
    ****
    ***
    **
    *
    """)

    for i in range(1, 5):
        print("A" * i)

    i = 5
    while True:
        print("V" * i)
        i -= 1

        if i == 0:
            break

if __name__ == "__main__":
    main()
