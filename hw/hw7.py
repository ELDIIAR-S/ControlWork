
import sqlite3

DB_NAME = "store.db"


def get_connection():
    """Открывает соединение с базой данных store.db"""
    return sqlite3.connect(DB_NAME)


def create_table():
    """Создаёт таблицу products, если она ещё не существует."""
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


# ---------- CREATE ----------
def create_product(name: str, price: float, quantity: int) -> None:
    """Добавляет новый товар в базу данных."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)",
        (name, price, quantity)
    )
    conn.commit()
    conn.close()
    print(f"Товар '{name}' добавлен.")


# ---------- READ ----------
def read_products() -> None:
    """Выводит все товары из базы данных."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, price, quantity FROM products")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("В базе пока нет товаров.")
        return

    print(f"{'ID':<5}{'Название':<20}{'Цена':<10}{'Кол-во':<10}")
    print("-" * 45)
    for row in rows:
        product_id, name, price, quantity = row
        print(f"{product_id:<5}{name:<20}{price:<10}{quantity:<10}")


# ---------- UPDATE ----------
def update_product(product_id: int, price: float) -> None:
    """Обновляет цену товара по его id."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE products SET price = ? WHERE id = ?",
        (price, product_id)
    )
    conn.commit()
    affected = cursor.rowcount
    conn.close()

    if affected:
        print(f"Цена товара с id={product_id} обновлена на {price}.")
    else:
        print(f"Товар с id={product_id} не найден.")


# ---------- DELETE ----------
def delete_product(product_id: int) -> None:
    """Удаляет товар из базы данных по id."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    affected = cursor.rowcount
    conn.close()

    if affected:
        print(f"Товар с id={product_id} удалён.")
    else:
        print(f"Товар с id={product_id} не найден.")


if __name__ == "__main__":
    create_table()

    # --- демонстрация работы CRUD ---
    print("\n--- CREATE ---")
    create_product("Ноутбук", 55000, 3)
    create_product("Мышь", 1200, 25)
    create_product("Клавиатура", 2500, 15)

    print("\n--- READ (все товары) ---")
    read_products()

    print("\n--- UPDATE (меняем цену товара с id=1) ---")
    update_product(1, 49999)
    read_products()

    print("\n--- DELETE (удаляем товар с id=2) ---")
    delete_product(2)
    read_products()
