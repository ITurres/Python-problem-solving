def main():
    height = get_height()
    draw_pyramid(height)


def get_height():
    while True:
        try:
            height = int(input("Height: "))
            if height > 0 and height < 9:
                return height
        except ValueError:
            pass


def draw_pyramid(height):
    for row in range(0, height, 1):
        for spaces in range(0, height, 1):
            if (row + spaces) < (height - 1):
                print(" ", end="")
            else:
                print("#", end="")
        print()


if __name__ == "__main__":
    main()
