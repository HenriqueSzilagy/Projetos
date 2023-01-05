def main():

    year = int(input("Type a Year: "))
    is_leap = is_leap_year(year)
    print(f"{year} is leap ? {is_leap}")


def is_leap_year(year):
    if not year % 4 == 0:
        return False
    elif year % 100 == 0:
        return False
    else:
        return True


if __name__ == "__main__":
    main()
