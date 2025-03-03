from pylogger import Logger
from pylogger.operators import cls
from binput import *
import shutil
from colorama import Fore, Back, init
from colorama.ansi import Cursor


columns = shutil.get_terminal_size().columns


class Texting:
    """
    Create a new class of Texting
    Args:
        names (list): Example: ["User", "AI"]
    """

    def __init__(self, roles: list):
        self.names = roles
        self._texts = []

    def add(self, role: str, content: str) -> None:
        self._texts.append(
            f"{" " * (columns - len(f"{role}: {content}")) if role == self.names[0] else ""}{f"{Back.LIGHTBLACK_EX}{role}" if not role == self.names[0] else f"{Back.LIGHTBLUE_EX}{role}"}: {content}"
        )

    def return_texts(self) -> list:
        return self._texts


if __name__ == "__main__":
    text = Texting(["User", "AI"])
    text.add("User", "hi")
    text.add("AI", "Hi")
    for item in text.return_texts():
        print(item)
