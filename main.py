from colorama import init, Fore

# Эта библиотека нужна для изменения цвета текста в консоли.
# Она позволяет делать вывод программы более наглядным.

init(autoreset=True)

print(Fore.GREEN + "Привет!")
print(Fore.YELLOW + "Это желтый текст.")
print(Fore.RED + "Это красный текст.")