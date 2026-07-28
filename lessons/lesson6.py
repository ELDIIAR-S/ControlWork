# #Декоратр
# def simple_decorator(func):
#     def wrapper():
#         print('До выполнения!!!')
#         func()
#         print('после выполнения!!')
#     return wrapper
#
# @simple_decorator
# def hello():
#     print('Hello')
#
# hello()

from colorama import Fore, Back, Style, init

init(autoreset=True)

print(Fore.RED + "Это красный текст")
print(Fore.GREEN + "Это зелёный текст")
print(Back.YELLOW + Fore.BLACK + "Чёрный текст на жёлтом фоне")
print(Style.BRIGHT + Fore.CYAN + "Это яркий голубой текст")
print(Style.NORMAL + "А это обычный текст без цвета")

from colorama import init, Fore

# Эта библиотека нужна для изменения цвета текста в консоли.
# Она используется, чтобы выводить сообщения разными цветами
# и делать программу более наглядной и удобной для чтения.

init(autoreset=True)

print(Fore.GREEN + "Привет!")
print(Fore.YELLOW + "Это желтый текст.")
print(Fore.RED + "Это красный текст.")