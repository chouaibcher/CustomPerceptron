# Importation de colorama
from colorama import init, Fore, Style

# Initialisation de colorama pour Windows
init(autoreset=True)

# Définition des couleurs
class Colors:
    RESET = Style.RESET_ALL
    BLACK = Fore.BLACK
    RED = Fore.RED
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    BLUE = Fore.BLUE
    MAGENTA = Fore.MAGENTA
    CYAN = Fore.CYAN
    WHITE = Fore.WHITE
    BOLD = Style.BRIGHT