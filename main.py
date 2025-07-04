import time

def print_heart():
    heart = [
        "  ***     ***  ",
        " *****   ***** ",
        "******* *******",
        " ************* ",
        "  ***********  ",
        "   *********   ",
        "    *******    ",
        "     *****     ",
        "      ***      ",
        "       *       "
    ]
    for line in heart:
        print(line)
        time.sleep(0.1)

def love_message(name="любимая"):
    print("\nЭто для тебя, " + name + " ❤️\n")
    time.sleep(1)
    print_heart()
    time.sleep(1)
    print("\nЯ ❤️ тебя больше, чем Python любит отступы.")
    print("И это навсегда.\n")

# Запускаем
love_message("солнышко")
