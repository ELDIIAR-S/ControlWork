from colorama import init, Fore


init(autoreset=True)

print(Fore.GREEN + "Привет, мир!")
print(Fore.YELLOW + "Это желтый текст.")
print(Fore.RED + "Это красный текст.")
print(Fore.BLUE + "Это синий текст.")

from faker import Faker

fake = Faker("ru_RU")  # указываем локаль "ru_RU", чтобы данные были на русском


def generate_users(count: int = 5) -> list[dict]:
    """Генерирует список пользователей со случайными данными."""
    users = []
    for i in range(1, count + 1):
        user = {
            "id": i,
            "name": fake.name(),
            "email": fake.email(),
            "phone": fake.phone_number(),
            "address": fake.address(),
            "job": fake.job(),
        }
        users.append(user)
    return users


def print_users(users: list[dict]) -> None:
    """Красиво выводит список пользователей в консоль."""
    for user in users:
        print(f"[{user['id']}] {user['name']}")
        print(f"    Email:   {user['email']}")
        print(f"    Телефон: {user['phone']}")
        print(f"    Адрес:   {user['address']}")
        print(f"    Работа:  {user['job']}")
        print("-" * 40)


if __name__ == "__main__":
    users = generate_users(5)
    print_users(users)
