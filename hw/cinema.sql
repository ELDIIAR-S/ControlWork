-- Включаем поддержку внешних ключей
PRAGMA foreign_keys = ON;

-- Удаляем старые таблицы при повторном запуске
DROP TABLE IF EXISTS reviews;
DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS users;

-- Таблица пользователей
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

-- Таблица фильмов
CREATE TABLE movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    genre TEXT NOT NULL
);

-- Таблица отзывов
CREATE TABLE reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    movie_id INTEGER NOT NULL,
    rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 10),

    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (movie_id) REFERENCES movies(id)
);

-- Добавляем 5 пользователей
INSERT INTO users (name)
VALUES
    ('Алексей'),
    ('Мария'),
    ('Иван'),
    ('Анна'),
    ('Дмитрий');

-- Добавляем 5 фильмов
INSERT INTO movies (title, genre)
VALUES
    ('Интерстеллар', 'Фантастика'),
    ('Титаник', 'Драма'),
    ('Джокер', 'Триллер'),
    ('Один дома', 'Комедия'),
    ('Матрица', 'Фантастика');

-- Добавляем 12 отзывов
-- У фильма «Матрица» пока нет отзывов,
-- чтобы проверить LEFT JOIN
INSERT INTO reviews (user_id, movie_id, rating)
VALUES
    (1, 1, 10),
    (1, 2, 8),
    (1, 4, 7),
    (2, 1, 9),
    (2, 2, 10),
    (2, 3, 8),
    (3, 1, 8),
    (3, 3, 9),
    (3, 4, 10),
    (4, 2, 9),
    (4, 3, 7),
    (5, 4, 8);


-- ============================================
-- ЧАСТЬ 2 — JOIN
-- ============================================

-- 1. Имя пользователя + фильм + оценка
SELECT
    users.name AS user_name,
    movies.title AS movie_title,
    reviews.rating
FROM reviews
JOIN users ON reviews.user_id = users.id
JOIN movies ON reviews.movie_id = movies.id
ORDER BY users.name, movies.title;


-- 2. Вывести все фильмы, даже если у них нет отзывов
SELECT
    movies.title,
    movies.genre,
    reviews.rating
FROM movies
LEFT JOIN reviews ON movies.id = reviews.movie_id
ORDER BY movies.title;


-- Более удобный вариант:
-- все фильмы и их средняя оценка
SELECT
    movies.title,
    movies.genre,
    ROUND(AVG(reviews.rating), 2) AS average_rating
FROM movies
LEFT JOIN reviews ON movies.id = reviews.movie_id
GROUP BY movies.id, movies.title, movies.genre
ORDER BY movies.title;


-- ============================================
-- ЧАСТЬ 3 — АГРЕГАЦИИ
-- ============================================

-- Средняя оценка всех отзывов
SELECT ROUND(AVG(rating), 2) AS average_rating
FROM reviews;

-- Максимальная оценка
SELECT MAX(rating) AS maximum_rating
FROM reviews;

-- Минимальная оценка
SELECT MIN(rating) AS minimum_rating
FROM reviews;

-- Все агрегаты одним запросом
SELECT
    ROUND(AVG(rating), 2) AS average_rating,
    MAX(rating) AS maximum_rating,
    MIN(rating) AS minimum_rating
FROM reviews;

-- Средняя, максимальная и минимальная оценка каждого фильма
SELECT
    movies.title,
    ROUND(AVG(reviews.rating), 2) AS average_rating,
    MAX(reviews.rating) AS maximum_rating,
    MIN(reviews.rating) AS minimum_rating
FROM movies
LEFT JOIN reviews ON movies.id = reviews.movie_id
GROUP BY movies.id, movies.title
ORDER BY movies.title;