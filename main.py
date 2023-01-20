from information_printer import welcoming_message

from utils.command_handler.command_handler import commands_handler
from utils.singletons.app_singleton import AppSingleton


def main():
    AppSingleton()
    welcoming_message()
    commands_handler()


if __name__ == "__main__":
    main()
