

def main():
    print("Select only one video game platform that is your favorite:")
    print("1. PlayStation")
    print("2. Xbox")
    print("3. Switch")
    print("4. Oculus")
    print("5. PC")
    choice = input("Please select number 1-5: ")

    if choice == '1':
        ps()
    elif choice == '2':
        xbox()
    elif choice == '3':
        switch()
    elif choice == '4':
        oculus()
    elif choice == '5':
        pc()
    else:
        print("That isn't a valid choice")


def ps():
    print("PlayStation is a great choice.")
    print("Sony makes some unbelievable things.")


def xbox():
    print("Xbox is a great choice.")
    print("Microsoft creates amazing things.")


def switch():
    print("Nintendo switch is so much fun.")
    print("Nintendo has been making systems for almost 40 years")


def oculus():
    print("Oculus Quest 2 is one of the best VR headsets around.")
    print("Facebook helped develop this VR headset.")


def pc():
    print("PC gaming is the new craze these days.")
    print("Pc games have come along way since the early days.")


main()
