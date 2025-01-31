from colorama.ansi import Cursor
from colorama import Fore, init

init()


def binput(prompt: str, color=Fore.BLUE):
    import shutil

    columns = shutil.get_terminal_size().columns
    prompt = "  " + prompt + "  "
    print(color + "╭" + prompt.center(columns - 24, "─") + ("─" * 22) + "╮")
    print(color + "\n" + "╰" + "".center(columns - 2, "─") + "╯")
    for i in range(2):
        print(Cursor.UP(2))
    print("".center(columns - 1) + "│", end="\r", flush=True)
    result = input("│  " + Fore.WHITE)
    print()
    return result


def bprint(prompt: str, name: str, color=Fore.BLUE):
    import shutil

    columns = shutil.get_terminal_size().columns
    prompt = "  " + prompt + "  "
    print(color + "╭" + prompt.center(columns - 24, "─") + ("─" * 22) + "╮")
    print(color + "\n" + "╰" + "".center(columns - 2, "─") + "╯")
    for i in range(2):
        print(Cursor.UP(2))
    print("".center(columns - 1) + "│", end="\r", flush=True)
    print("│  " + Fore.WHITE + name)
    print()


if __name__ == "__main__":
    import os

    os.system("cls")
    print(binput("Enter your name"))
    bprint("test", "Lorem Ipsum Sit Amet Dolor")
