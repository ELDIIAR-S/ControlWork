from colorama import Fore, Back, Style, init

init(autoreset=True)

print(Fore.RED + "Это красный текст")
print(Fore.GREEN + "Это зелёный текст")
print(Back.YELLOW + Fore.BLACK + "Чёрный текст на жёлтом фоне")
print(Style.BRIGHT + Fore.CYAN + "Это яркий голубой текст")
print(Style.NORMAL + "А это обычный текст без цвета")

