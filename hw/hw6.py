from colorama import init, Fore, Back, Style

init(autoreset=True)


def show_status(message: str, status: str = "info") -> None:
    """Выводит сообщение разным цветом в зависимости от типа статуса."""
    colors = {
        "info": Fore.CYAN,
        "success": Fore.GREEN,
        "warning": Fore.YELLOW,
        "error": Fore.RED,
    }
    color = colors.get(status, Fore.WHITE)
    print(color + f"[{status.upper()}] {message}" + Style.RESET_ALL)


def main() -> None:
    print(Style.BRIGHT + Fore.MAGENTA + "=== Демонстрация библиотеки colorama ===")
    print()

    show_status("Программа запущена", "info")
    show_status("Файл успешно загружен", "success")
    show_status("Проверьте настройки конфигурации", "warning")
    show_status("Не удалось подключиться к серверу", "error")

    print()
    print(Back. BLACK + Fore.WHITE + " Пример текста с цветным фоном " + Style.RESET_ALL)


if __name__ == "__main__":
    main()