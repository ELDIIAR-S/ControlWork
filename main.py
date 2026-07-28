from colorama import init, Fore

# Эта библиотека нужна для изменения цвета текста в консоли.
# Она позволяет делать вывод программы более красивым и удобным для чтения.

init(autoreset=True)

print(Fore.GREEN + "Привет, мир!")
print(Fore.YELLOW + "Это желтый текст.")
print(Fore.RED + "Это красный текст.")
print(Fore.BLUE + "Это синий текст.")