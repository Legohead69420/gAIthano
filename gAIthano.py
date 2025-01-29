from pylogger import Logger
from pylogger.operators import cls
import gAIthano.gAIthano.IOMng as io
from gAIthano.gAIthano.binput import *
from time import strftime, sleep
from time import perf_counter as cont
from colorama import Fore, Back, init

init(autoreset=True)
from ollama import chat
from ollama import ChatResponse

loaderlist = ["⠄", "⠆", "⠇", "⠋", "⠙", "⠸", "⠰", "⠠", "⠰", "⠸", "⠙", "⠋", "⠇", "⠆"]

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
        message = binput("Enter your prompt")

        if message == "/bye":
            exit(cls())

        elif message == "/?" or message == "/help":
            cls()
            helpmsg = """
    Available Commands:
      /clear          Clear session context
      /bye            Exit
      /?, /help       Help for a command\n"""
            print(helpmsg)
            return

        elif message == "/clear":
            messages = [{"role": "system", "content": baseprompt}]
            return

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
        print(f"Model took {e:0.3f} seconds")
        print(response["message"]["content"])
        io.speak(response["message"]["content"])
        print()


if __name__ == "__main__":
    runmodel()
