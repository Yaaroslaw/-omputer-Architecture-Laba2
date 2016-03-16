from controller import *


def menu():  # Взаємодія з користувачем
    print(" 1.Show ")
    print("  _________")
    print(" 2.Add day ")
    print("  _________")
    print(" 3.Add month")
    print("  _________")
    print(" 4.Exit ")
    choice = input("Your choice: ")
    if choice == "1":
        show_month()
        print("If you want to continue enter 1, else enter any key")
        choice2 = input("Your choice: ")
        if choice2 == "1":
            menu()
        else:
            exit()
    if choice == "2":
        print("Months in the weather-blog: ")
        for i in season.keys():
            print("- " + i)
        name = input("Please, type the name of "


                     "the month to which you want to add your observation:  ")
        param(name)
        print("If you want to continue enter 1, else enter any key ")
        choice2 = input("Your choice: ")
        if choice2 == "1":
            menu()
        else:
            exit()
    if choice == "3":
        name = input("Please, type the name of the month ")
        add_month(name)
        print("Do you want to add days to this month? ")
        day_choice = input("Enter 1 to add, enter 2 to go back to menu ")
        if day_choice == "1":
            param(name)
            print("If you want to continue enter 1, else enter any key ")
            choice2 = input("Your choice: ")
            if choice2 == "1":
                menu()
            else:
                exit()
        elif day_choice == "2":
            menu()
    if choice == "4":
            exit()


if __name__ == '__main__':
    season = creation_blog()
    menu()
