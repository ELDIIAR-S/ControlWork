import sqlite3

# Создание базы данных
connection = sqlite3.connect("store.db")
cursor = connection.cursor()


# Создание таблицы products
def create_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        quantity INTEGER NOT NULL
    )
    """)
    connection.commit()


# 1. CREATE — добавление товара
def create_product(name, price, quantity):
    cursor.execute("""
    INSERT INTO products (name, price, quantity)
    VALUES (?, ?, ?)
    """, (name, price, quantity))

    connection.commit()
    print("Товар добавлен")


# 2. READ — получение всех товаров
def read_products():
    cursor.execute("SELECT * FROM products")

    products = cursor.fetchall()

    for product in products:
        print(product)


# 3. UPDATE — обновление цены товара по id
def update_product(id, price):
    cursor.execute("""
    UPDATE products
    SET price = ?
    WHERE id = ?
    """, (price, id))

    connection.commit()
    print("Цена обновлена")


# 4. DELETE — удаление товара по id
def delete_product(id):
    cursor.execute("""
    DELETE FROM products
    WHERE id = ?
    """, (id,))

    connection.commit()
    print("Товар удалён")


# Создание таблицы
create_table()


# Проверка работы CRUD

create_product("Телефон", 50000, 10)
create_product("Наушники", 5000, 25)
create_product("Монитор", 30000, 7)


print("\nВсе товары:")
read_products()


print("\nОбновление цены:")
update_product(1, 55000)


print("\nПосле обновления:")
read_products()


print("\nУдаление товара:")
delete_product(2)


print("\nПосле удаления:")
read_products()


# Закрытие базы данных
connection.close()