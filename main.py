import sqlite3

DB_NAME = "store.db"


def get_connection():
    """Создаёт соединение с базой данных store.db"""
    return sqlite3.connect(DB_NAME)


def create_table():
    """Создаёт таблицу products, если она ещё не существует"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()


# ---------------------- CREATE ----------------------
def create_product(name, price, quantity):
    """Добавляет новый товар в базу данных"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)",
        (name, price, quantity)
    )
    conn.commit()
    conn.close()
    print(f"[CREATE] Товар '{name}' добавлен.")


# ---------------------- READ ----------------------
def read_products():
    """Выводит все товары из базы данных"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("[READ] Товаров пока нет.")
        return

    print("[READ] Список товаров:")
    print("-" * 50)
    print(f"{'ID':<5}{'Название':<20}{'Цена':<15}{'Кол-во':<10}")
    print("-" * 50)
    for row in rows:
        id_, name, price, quantity = row
        price_str = f"{price:,.0f} ₽".replace(",", " ")  # 75000 -> "75 000 ₽"
        print(f"{id_:<5}{name:<20}{price_str:<15}{quantity:<10}")
    print("-" * 50)


# ---------------------- UPDATE ----------------------
def update_product(id, price):
    """Обновляет цену товара по id"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE id = ?", (id,))
    if cursor.fetchone() is None:
        print(f"[UPDATE] Товар с id={id} не найден.")
        conn.close()
        return

    cursor.execute(
        "UPDATE products SET price = ? WHERE id = ?",
        (price, id)
    )
    conn.commit()
    conn.close()
    print(f"[UPDATE] Цена товара с id={id} обновлена на {price}.")


# ---------------------- DELETE ----------------------
def delete_product(id):
    """Удаляет товар по id"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE id = ?", (id,))
    if cursor.fetchone() is None:
        print(f"[DELETE] Товар с id={id} не найден.")
        conn.close()
        return

    cursor.execute("DELETE FROM products WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    print(f"[DELETE] Товар с id={id} удалён.")


# ---------------------- ДЕМОНСТРАЦИЯ ----------------------
if __name__ == "__main__":
    create_table()

    print("\n=== Добавление товаров ===")
    create_product("Ноутбук", 75000, 5)
    create_product("Мышка", 2000, 20)
    create_product("Клавиатура", 3000, 10)
    create_product("Монитор", 18000, 7)
    create_product("Наушники", 4500, 12)
    create_product("Флешка", 1200, 30)

    print("\n=== Чтение всех товаров ===")
    read_products()

    print("\n=== Изменение цены товара с id=2 ===")
    update_product(2, 1800)
    read_products()

    print("\n=== Удаление товара (id=6) ===")
    delete_product(6)
    read_products()


# Подключение к базе данных

# from colorama import init, Fore, Back, Style
#
# init(autoreset=True)
#
#
# def show_status(message: str, status: str = "info") -> None:
#     """Выводит сообщение разным цветом в зависимости от типа статуса."""
#     colors = {
#         "info": Fore.CYAN,
#         "success": Fore.GREEN,
#         "warning": Fore.YELLOW,
#         "error": Fore.RED,
#     }
#     color = colors.get(status, Fore.WHITE)
#     print(color + f"[{status.upper()}] {message}" + Style.RESET_ALL)
#
#
# def main() -> None:
#     print(Style.BRIGHT + Fore.MAGENTA + "=== Демонстрация библиотеки colorama ===")
#     print()
#
#     show_status("Программа запущена", "info")
#     show_status("Файл успешно загружен", "success")
#     show_status("Проверьте настройки конфигурации", "warning")
#     show_status("Не удалось подключиться к серверу", "error")
#
#     print()
#     print(Back. BLACK + Fore.WHITE + " Пример текста с цветным фоном " + Style.RESET_ALL)
#
#
# if __name__ == "__main__":
#     main()