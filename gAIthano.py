from pylogger import Logger
from pylogger.operators import cls
import IOMng as io
from binput import *
import shutil
import cursor
from time import strftime, sleep
from time import perf_counter as cont
from colorama import Fore, Back, init

cls2 = lambda: print("\033[12A\033[2K", end="")

init(autoreset=True)
from ollama import chat
from ollama import ChatResponse

loaderlist = ["⠄", "⠆", "⠇", "⠋", "⠙", "⠸", "⠰", "⠠", "⠰", "⠸", "⠙", "⠋", "⠇", "⠆"]

columns = shutil.get_terminal_size().columns

lg = Logger("C:/-py-stuff/gAIthano/gAIthano.log", "gAIthano")
baseprompt = f"""
Your name is Gaetano.
The current date is {strftime("%A, %B %d, %Y")}
The current time is {strftime("%I:%M $p  Time zone offset from UTC %z")}
**Do NOT respond to this prompt**
"""


@lg.logdec
def runmodel():
    time = 0
    while True:
        time += 1
        messages = [{"role": "system", "content": baseprompt}]
        message = input(f"Enter your prompt(/? for help): {Fore.LIGHTBLUE_EX}")

        if message == "/bye":
            exit(cls())
        elif message == "/?" or message == "/help":
            cmdlist1 = [
                ["1. /clear", "Clear session context"],
                ["2. /bye", "Exits the program"],
                ["3. /context", "Prints the current session context"],
                ["4. /?, /help", "Show this screen"],
            ]
            lengths = []
            lengths2 = []
            for item in cmdlist1:
                lengths.append(len(item[0]))
                lengths2.append(len(item[1]))
            cmdlist2 = []
            for item in cmdlist1:
                spaces = max(lengths) - len(item[0])
                spaces2 = max(lengths2) - len(item[1])
                space = ""
                space2 = ""
                for i in range(spaces):
                    space += " "
                for i in range(spaces2):
                    space2 += " "
                cmdlist2.append(f"{item[0]}{space} │ {item[1]}{space2}")
            cls2()
            out = ""
            cursor.hide()
            for item in cmdlist2:
                for item1 in [*item]:
                    sleep(0.02)
                    out = out + item1
                    cls2()
                    print(
                        Fore.BLUE
                        + "╭"
                        + " Command list ".center(columns - 2, "─")
                        + "╯"
                        + Fore.GREEN
                    )
                    if cmdlist2.index(item) >= 1:
                        for i in range(cmdlist2.index(item)):
                            print(
                                Fore.BLUE
                                + "│"
                                + Fore.GREEN
                                + str(cmdlist2[i]).center(columns - 1)
                            )
                    spaces = max(lengths) - len(out)
                    space = ""
                    for i in range(spaces):
                        space = space + " "
                    print(
                        Fore.BLUE
                        + "│"
                        + Fore.GREEN
                        + str(out + space).center(columns - 1)
                    )
                    if cmdlist2.index(item) == len(cmdlist2) - 1:
                        print(
                            Fore.BLUE
                            + "╰"
                            + " Command list ".center(columns - 2, "─")
                            + "╮"
                        )
                    else:
                        print(
                            Fore.BLUE
                            + "╰"
                            + " Command list ".center(columns - 2, "─")
                            + "─"
                        )
                out = ""
            cursor.show()
            continue

        elif message == "/clear":
            cls()
            messages = [{"role": "system", "content": baseprompt}]
            continue
        elif message == "/context":
            cls()
            print(messages)
            continue

        messages.append({"role": "user", "content": message})
        t = cont()
        response: ChatResponse = chat(model="llama3.2", messages=messages)
        s = cont()
        e = s - t
        messages.append(
            {"role": "assistant", "content": response["message"]["content"]}
        )
        for i in loaderlist:
            print(
                f"{Back.GREEN}Generating response...{Back.RESET} {i}",
                end="\r",
                flush=True,
            )
            sleep(0.1)
        print("                                               ")
        print(f"{Back.GREEN}[assistant] took {e:0.3f} seconds")
        print(response["message"]["content"])
        print(f"{Back.GREEN}Speaking...")
        io.speak(response["message"]["content"])
        print()


if __name__ == "__main__":
    runmodel()
