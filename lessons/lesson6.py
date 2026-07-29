from colorama import Fore, Style, init

init()

# Эта библиотека нужна для изменения цвета текста в консоли.
# Она используется, чтобы сделать вывод программы более удобным и понятным.

print(Fore.GREEN + "Программа запущена успешно!" + Style.RESET_ALL)

print(Fore.BLUE + "Используется библиотека colorama" + Style.RESET_ALL)

print(Fore.RED + "Это сообщение красного цвета" + Style.RESET_ALL)