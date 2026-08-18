def get_chinese_zodiac(year):
    zodiacs = [
        ("Monkey"),
        ("Rooster"),
        ("Dog"),
        ("Pig"),
        ("Rat"),
        ("Ox"),
        ("Tiger"),
        ("Rabbit"),
        ("Dragon"),
        ("Snake"),
        ("Horse"),
        ("Goat"),
    ]

    # The 12-year cycle repeats, with year % 12 mapping directly to the zodiac index
    index = year % 12
    return zodiacs[index]


def main():
    try:
        user_input = input("Enter your birth year (e.g., 1998): ")
        year = int(user_input)

        if year <= 0:
            print("Please enter a valid positive AD year.")
            return

        sign = get_chinese_zodiac(year)
        print(f"\nYour birth year is {year}.")
        print(f"Your Chinese Zodiac sign is the {sign}!")
        print("Note: The traditional Lunar New Year usually begins in late January or February.")

    except ValueError:
        print("Invalid input. Please enter a numerical year.")


if __name__ == "__main__":
    main()