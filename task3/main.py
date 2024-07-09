import sys
from pathlib import Path
from colorama import init, Fore

init(autoreset=True)

def list_directory(directory, indent_level=0):
    if not directory.exists():
        print(Fore.RED + f"Помилка: Шлях '{directory}' не існує.")
        return
    if not directory.is_dir():
        print(Fore.RED + f"Помилка: Шлях '{directory}' не є директорією.")
        return

    for item in directory.iterdir():
        indent = ' ' * indent_level
        if item.is_dir():
            print(Fore.BLUE + f"{indent}{item.name}/")
            list_directory(item, indent_level + 4) 
        else:
            print(Fore.GREEN + f"{indent}{item.name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.RED + "Використання: python script.py <шлях_до_директорії>")
        sys.exit(1)

    directory_path = Path(sys.argv[1])
    list_directory(directory_path)
