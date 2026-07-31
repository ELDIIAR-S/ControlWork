import asyncio
import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        execution_time = time.perf_counter() - start_time
        print(f"Функция {func.__name__} работала {execution_time:.2f} секунды")

        return result

    return wrapper


def async_timer(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        result = await func(*args, **kwargs)

        execution_time = time.perf_counter() - start_time
        print(f"Функция {func.__name__} работала {execution_time:.2f} секунды")

        return result

    return wrapper


@timer
def calculate_sum(n):
    return sum(range(n))


@async_timer
async def download_data():
    await asyncio.sleep(2)
    return "Данные загружены"


async def main():
    result_sum = calculate_sum(1_000_000)
    print(result_sum)

    result_data = await download_data()
    print(result_data)


if __name__ == "__main__":
    asyncio.run(main())