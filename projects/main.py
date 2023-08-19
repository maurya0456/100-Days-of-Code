def check_leap_year():
    yr = int(input("Enter year val to check "))
    is_leap_year = False
    if yr % 4 == 0:
        if yr % 100 == 0:
            if yr % 400 == 0:
                is_leap_year = True
            else:
                is_leap_year = False
        else:
            is_leap_year = True
    else:
        is_leap_year = False

    if is_leap_year:
        print("{0} is a leap year".format(yr))
    else:
        print("{0} is a not leap year".format(yr))


def love_calculator():
    print("Welcome to the Love Calculator")

    name1 = input("What's your name? ").lower()
    name2 = input("What's their name? ").lower()

    letter_of_true_occurs = name1.count('t') + name1.count('r') + name1.count('u') + name1.count('e') + name2.count(
        't') + name2.count('r') + name2.count('u') + name2.count('e')

    letter_of_love_occurs = name1.count('l') + name1.count('o') + name1.count('v') + name1.count('e') + name2.count(
        'l') + name2.count('o') + name2.count('v') + name2.count('e')

    final_val = str(letter_of_true_occurs) + str(letter_of_love_occurs)
    integer_final_val = int(final_val)
    if integer_final_val < 10 or integer_final_val > 90:
        print(f"Your score is {integer_final_val}, you go together like coke and mentos")
    elif 40 <= integer_final_val <= 50:
        print(f"Your score is {integer_final_val}, you are alright together")
    else:
        print(f"Your score is {integer_final_val}")


if __name__ == '__main__':
    love_calculator()
    check_leap_year()
