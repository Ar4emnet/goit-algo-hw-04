from colorama import Fore

def dir_color(name):
    return f"{Fore.YELLOW}{name}{Fore.RESET}"

def files_color(name):
    return f"{Fore.GREEN}{name}{Fore.RESET}"
